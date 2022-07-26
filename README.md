# symbolFilter

You will develop a small piece of code that accepts a comma delimited list of tags (words/tokens - characters, numbers,
some symbols like $£%& but not a comma) and must return an array of tags. The preceding and proceeding commas should be
removed, white spaces preceding the first tag must be removed, white spaces proceeding the last tag must be removed, and
contiguous series of words separated with spaces and ended with a comma should be treated as a single tag

Examples of the rules are as follows

"java" must return ["java"]

"java, python" must return ["java", "python"]

"  java" must return ["java"]

",java" must return ["java"]

"java," must return ["java"]

"java byte code, python" must return ["java byte code", "python"]