import ast
import re

NAUGHTY_WORDS = {
    # Common words taken too far
    'bossy': 'Assertive, but Karen doesn’t like it.',
    'rockstar': 'We are not in a band, this is the workplace.',
    'guru': 'Karen prefers certified experts.',
    'ninja': 'This is not a dojo.',
    'wizard': 'We use real tools, not magic.',
    'kickass': 'That’s too aggressive.',
    'crushing it': 'You’re not literally crushing anything.',
    'hustle': 'We’re all about work-life balance here.',
    'disrupt': 'We prefer not to disturb things.',
    'game-changer': 'We don’t play games here.',

    # Words that sound vaguely rebellious
    'grind': 'Work is not about grinding.',
    'grit': 'Too harsh for a soft environment.',
    'lean in': 'Karen wants you to sit up straight.',
    'kill': 'Figurative language is a no-go.',
    'dominate': 'Karen feels uncomfortable with power dynamics.',

    # Buzzwords that have run their course
    'synergy': 'We prefer “working together.”',
    'circle back': 'Just say you’ll respond later.',
    'touch base': 'You’re not a baseball player.',
    'low-hanging fruit': 'Karen thinks it’s too lazy.',
    'move the needle': 'Let’s avoid sharp objects.',
    'deep dive': 'We’re not scuba diving.',
    'ping': 'Please, no techy jargon.',

    # Words related to hierarchy (because Karen doesn’t like authority)
    'superior': 'Karen believes we’re all equals.',
    'subordinate': 'Too demeaning, we prefer “teammate.”',
    'overlord': 'It’s not a dictatorship here.',
    'underling': 'Absolutely not, we’re all equals.',
    'minion': 'You’re not a cartoon character.',
    'chief': 'C-suite? Let’s use “executive” instead.',

    # Informal language
    'dude': 'Too casual for the office.',
    'bro': 'We’re a family, not a frat.',
    'fam': 'You’re not my family.',
    'slay': 'No, you’re not slaying anything.',
    'bae': 'Completely inappropriate for work.',
    'lol': 'Not everything is funny.',
    'omg': 'Karen doesn’t allow acronyms.',

    # Words Karen finds threatening or too strong
    'exploit': 'Let’s not use that word, it sounds mean.',
    'attack': 'Calm down, it’s just a presentation.',
    'destroy': 'Karen prefers to “reorganize.”',
    'obliterate': 'Whoa, too extreme.',
    'hammer': 'We use tools, not violence.',
    'terminate': 'Sounds too final, try “end” instead.',
    'shoot': 'Nope, no shooting here, even figuratively.',

    # Words that imply excitement or emotion
    'passion': 'Sounds a bit too intense for Karen.',
    'obsessed': 'Karen likes work-life balance.',
    'fanatic': 'Let’s keep it professional.',
    'love': 'Too much emotion for the workplace.',

    # Words implying too much efficiency
    'machine': 'You’re not a robot, please relax.',
    'automate': 'That sounds like replacing people with machines.',
    'productivity': 'We don’t push for *too much* productivity.',

    # Overly positive words that annoy Karen
    'awesome': 'Overly enthusiastic.',
    'amazing': 'Tone it down a bit.',
    'epic': 'Not every task is an adventure.',

    # Miscellaneous absurd words
    'rad': 'It’s not the 90s.',
    'cool': 'Work isn’t about being cool.',
    'fired up': 'Calm down, please.',
    'beast mode': 'No need to unleash your inner animal.',
    'hacker': 'Are you breaking into something?',

    # Gendered or role-based language
    'man up': 'Gendered language not allowed.',
    'woman power': 'We prefer “team power.”',
    'guys': 'Too gender-specific.',
    'ladies': 'Again, too gender-specific.',
    'girlfriend': 'Karen thinks this is too personal.',
    'boyfriend': 'Let’s leave personal life at home.',

    # Miscellaneous HR-approved words Karen dislikes
    'problem': 'Let’s call it an “opportunity” instead.',
    'issue': 'Too negative, call it a “challenge.”',
    'risk': 'We prefer the word “opportunity.”',
    'failure': 'Nobody fails, we just “learn.”',
    'mistake': 'We call those “learning experiences.”',

    # IT/Tech Jargon Karen Doesn’t Understand
    'python': 'Please, no hacker talk.',
    'burnout': 'We don’t talk about exhaustion here.',
    'deploy': 'Too technical, say “install.”',
    'root cause': 'It’s too technical for Karen’s liking.',
    'bug': 'Karen prefers “unexpected feature.”',
    'whitelist': 'Karen prefers more inclusive language. Use "allowlist" instead.',
    'blacklist': 'Karen prefers more inclusive language. Use "blocklist" instead.',

    # Anything slightly fun or non-conventional
    'party': 'We’re not throwing parties in the office.',
    'fun': 'Work is serious, not fun.',
    'happy hour': 'Drinking? Not on Karen’s watch.',
    'lunch break': 'You can have a break, but don’t mention it.',
    'vacation': 'Work comes first, always.',
}


FIREABLE_WORDS = {
    'fired': 'Using the word "fired" will get you fired!',
    'drunk': 'Drinking on the job? Immediate termination!',
    'hungover': 'Admitting to being hungover at work is grounds for termination.',
    'lazy': 'We don’t tolerate calling anyone lazy here.',
    'stupid': 'Calling things or people stupid is unacceptable.',
    'idiot': 'Using insulting language like "idiot" is fireable.',
    'failure': 'Talking about failure in this way is unacceptable.',
    'hate': 'Hate speech of any kind is not tolerated.',
    'illegal': 'Do not mention anything illegal at work.',
    'cheat': 'No cheating is allowed in the workplace.',
    'bribe': 'Mentioning bribery will lead to termination.',
    'violence': 'Violence is a fireable offense.',
    'harass': 'Harassment in any form results in termination.',
    'racist': 'Any reference to racism is immediately unacceptable.',
    'sexist': 'Sexism is a fireable offense.',
    'corrupt': 'Mentioning corruption is grounds for termination.',
    'incompetent': 'Calling someone or something incompetent is fireable.',
    'unethical': 'Unethical behavior leads to termination.',
    'toxic': 'Mentioning a toxic work environment is not tolerated.',
    'master': 'The term "master" is outdated and inappropriate in this context.',
    'slave': 'The term "slave" is offensive. Please use "secondary" or "replica" instead.',
}


def check_naughty_words(line):
    """Check if the line contains any naughty words or fire-able offenses."""
    violations = []
    # Check for naughty words (full word match only)
    for word, rule in NAUGHTY_WORDS.items():
        # Use regular expression to match whole words only
        if re.search(rf'\b{re.escape(word)}\b', line):
            violations.append((word, rule, "warning"))

    # Check for fire-able words (full word match only)
    for word, rule in FIREABLE_WORDS.items():
        # Use regular expression to match whole words only
        if re.search(rf'\b{re.escape(word)}\b', line):
            violations.append((word, rule, "termination"))

    return violations


def check_custom_lint_rules(filepath):
    violations = []

    with open(filepath, 'r') as f:
        lines = f.readlines()

    tree = ast.parse("".join(lines), filename=filepath)

    # 2. Check for function names that are not complete sentences
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            if not (re.search(r'\s', func_name) and func_name.endswith('.')):
                violations.append((
                    node.lineno,
                    lines[node.lineno - 1].strip(),  # Add the offending line content
                    "Grammar Nazi",                        # Indicate this is a custom rule
                    'Function names should be complete sentences with proper punctuation.',
                    'bless-heart'
                ))

    # 3. Check for variables with the word 'temp'
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if 'temp' in node.id.lower():
                violations.append((
                    node.lineno,
                    lines[node.lineno - 1].strip(),
                    "Hi-Tech Karen",
                    "No temporary variables allowed. Everything should have a permanent purpose.",
                    'bless-heart'
                ))

    # 5. Check for single-letter variable names
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and len(node.id) == 1:
            violations.append((
                node.lineno,
                lines[node.lineno - 1].strip(),
                "Grammar Nazi",
                'Single-letter variables are lazy. Use descriptive names.',
                'bless-heart'
            ))

    # 7. Check for list comprehensions (avoid Pythonic idioms)
    for node in ast.walk(tree):
        if isinstance(node, ast.ListComp):
            violations.append((
                node.lineno,
                lines[node.lineno - 1].strip(),
                "Hi-Tech Karen",
                'Avoid Pythonic shortcuts like list comprehensions. They are too clever for their own good.',
                'bless-heart'
            ))

    return violations
