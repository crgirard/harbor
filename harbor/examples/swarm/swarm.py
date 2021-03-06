'''
harbor: spec
# Swarm
'''

'''
harbor: spec/ranges
{Ranges}[section]
'''

'''
harbor: spec/ranges/operations
{Operations}[subsection]
'''

'''
harbor: spec/ranges/operations/creating
{Creating}[subsubsection]

Range notation in Swarm is a more compact way of specifying lists that are composed of integers and follow a linear pattern.
`[a:b:c]` is the canonical form, but many variations exist. This form defines a sequence that starts with `a`, steps by `b`, and ends with a value `n` where `n <= c`. Examples:
- `[0:1:8]` is equivalent to `[0,1,2,3,4,5,6,7,8]`
- `[0:1:0]` is equivalent to `[0]`
- `[0:2:6]` is equivalent to `[0,2,4,6]`
- `[0:2:5]` is equivalent to `[0,2,4]`
- `[6:-2:-4]` is equivalent to `[6,4,2,0,-2,-4]`

`b` can be omitted (`[a:c]`), and defaults to `1` if `a < c` or `-1` if `a > c`.
If `a == c`, `[a:b:c]` returns `[a]` no matter the value or existence of `b`.

Additionally, either `[` or `]` may be exchanged for the corresponding parenthesis, which makes that bound exclusive rather than inclusive. For example:

- `[4:7]` = `[4,5,6,7]`
- `[4:7)` = `[4,5,6]`
- `(4:7]` = `[5,6,7]`
- `(4:7)` = `[5,6]`

The same applies where `b != 1`:
- `(4:2:8)` = `[6]`
- `(0:3:12]` = `[3,6,9,12]`
`(` works by simply skipping what would have been the first element if `[` had been used.
`)` works by ensuring that the final element in the sequence is less than `c`

If `a == c` and one or both bounds are exclusive, an empty array is the result:
- `[5:b:5]` = `[5]` for any `b`
- `[5:b:5)` = `[]` for any `b`
- `(5:b:5]` = `[]` for any `b`
- `(5:b:5)` = `[]` for any `b`
'''

'''
harbor: spec/ranges/properties
{Properties}[subsection]

{.length}[method] Returns the number of elements in the range
'''

'''
harbor: spec/ranges/methods
{Methods}[subsection]

{a.overlap(b)}[method] Returns a new `Range` that contains only the elements in both `a` and `b`.
`[1:7].overlap([4:9])` = `[4:7]`
`[1:2:7].overlap([4:2:9])` = `[]`

{.normalize()}[method} Converts the `Range`, in-place, to a normalized form, ie inclusive on both ends, and with `a` and `c` as close as possible.
`(4:8).normalize()` = `[5:7]`
`(6:2].normalize()` = `[5:2]`
`(0:3:14].normalize()` = `[3:3:12]`
`(-2:-5:-105]` = `[-7:-5:-102]`
'''








'''
harbor: spec/arrays
---

{Arrays}[section]
'''

'''
harbor: spec/arrays/operations
{Operations}[subsection]
'''

'''
harbor: spec/arrays/operations/creating
{Creating}[subsubsection]

Arrays are created by putting a sequence of comma-separated values between square brackets:

`[1,2,3,'apple',5+5]`

All provided expressions are reduced, ie `[1,2,3,3+1,3+2,3+3]` is equivalent to `[1,2,3,4,5,6]`

Array elements are numbered in two schemes:
- From the left increasing from 0
- From the right decreasing from -1

For example, given the array `a = [5,7,42,6,1,-6,7,-4,9,13]`:

|Value           |5   |7   |42  |6   |1   |-6  |7   |-4  |9   |13  |
|            :---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|Index from left |0   |1   |2   |3   |4   |5   |6   |7   |8   |9   |
|Index from right|-10 |-9  |-8  |-7  |-6  |-5  |-4  |-3  |-2  |-1  |
'''

'''
harbor: spec/arrays/operations/accessing
{Accessing}[subsubsection]

Either scheme can be used to access array elements:

`a[0]` = `5`
`a[-10]` = `5`

`a[2]` = `42`
`a[-8]` = `42`

`a[9]` = `13`
`a[-1]` = `13`

Multiple elements can be chosen, separated by commas:

- `a[4,7,-9,3]` = `[1,-4,7,6]`

`Range` can also be used to access elements:

`a[2:5)` = `[42,6,1]`
`a[7:-2:1]` = `[-4,-6,6,7]`

When using a `Range` to specify an array subset, specifying `a` and `c` becomes optional, since we're working with a bounded interval already.

- If `a` is omitted and `b` is positive, the sequence starts at element `0`
`[2,7,3,6,4,5][:1:3]` = `[2,7,3,6]`
`[2,7,3,6,4,5][::3]` = `[2,7,3,6]`

- If `a` is omitted and `b` is negative, the sequence starts at element `-1`
`[2,7,3,6,4,5][:-1:3]` = `[5,4,6]`

- If `c` is omitted and `b` is positive, the sequence stops at or before the last element
`[2,7,3,6,4,5][3:1:]` = `[6,4,5]`
`[2,7,3,6,4,5][3::]` = `[6,4,5]`

- If `c` is omitted and `b` is negative, the sequence stops at or before the first element
`[2,7,3,6,4,5][3:-1:]` = `[6,3,7,2]`

- If both `a` and `c` are omitted and `b` is positive:
`[2,7,3,6,4,5][:1:]` = `[2,7,3,6,4,5]`
`[2,7,3,6,4,5][::]` = `[2,7,3,6,4,5]`
`[2,7,3,6,4,5][:2:]` = `[2,3,4]`

- If both `a` and `c` are omitted and `b` is negative:
`[2,7,3,6,4,5][:-1:]` = `[5,4,6,3,7,2]`
`[2,7,3,6,4,5][:-2:]` = `[5,6,7]`
'''

'''
harbor: spec/arrays/operations/packing
{Packing}[subsubsection]

`t = 1,2,3,'apple'` sets `t` to `[1,2,3,'apple']`
'''

'''
harbor: spec/arrays/operations/unpacking
{Unpacking}[subsubsection]

`a,b,c,d = [1,2,3,'apple']` sets `a` to `1`, etc.

The two operations will reverse each other:
```
t = 1,2,3
a,b,c = t
```
'''

'''
harbor: spec/arrays/properties
{Properties}[subsection]

{.length}[method] Returns the length of the array
'''

'''
harbor: spec/arrays/methods
{methods}[subsection]

{.append(e)}[method] Adds item `e` to the end of the array.
{.index(e)}[method] Returns the indices where the element equals `e`.
{.insert(e,i)}[method] Inserts element `e` at position `i`. `.insert('a',0)` makes `'a'` the new first element.
{.pop([i])}[method] Removes and returns the element at index `i`. If `i` is omitted, it defaults to the last item.
{.sort()}[method]
{a[:-1:]}[method] Returns a reversed copy of array `a`.
'''





'''
harbor: spec/strings
---

{Strings}[section]

Strings are represented as linked lists (maybe) until they are sent to another agent.

'''

'''
harbor: spec/strings/operations
{Operations}[subsection]
'''

'''
harbor: spec/strings/operations/creating
{Creating}[subsubsection]
'''

'''
harbor: spec/strings/operations/concatenating
{Concatenating}[subsubsection]
```
a = 'ap' + 'ple'

b = 'ap'
b = b + 'ple'

c = 'ap'
c += 'ple'

d = ''
d += 'app'
d += 'le'

e = 'ple'
e = 'ap' + e

f = ''
for i in 'apple':
    f += i
```
'''

'''
harbor: spec/strings/operations/querying
{Querying}[subsubsection]

- `'sub' in 'substring'` returns `true`
- `'strings' in 'substring'` returns `false`
- `'substring' in 'sub'` returns `false`
- `'string' in 'string'` returns `true`
'''

'''
harbor: spec/strings/operations/accessing
{Accessing}[subsubsection]

|Value           |t   |e   |s   |t   |s   |t   |r   |i   |n   |g   |
|            :---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|Index from left |0   |1   |2   |3   |4   |5   |6   |7   |8   |9   |
|Index from right|-10 |-9  |-8  |-7  |-6  |-5  |-4  |-3  |-2  |-1  |

Accessing string elements is identical to accessing array elements, with the exception that the output is returned as a string:

#### `string[a]`
- `'teststring'[0]` returns `'t'`
- `'teststring'[1]` returns `'e'`
- `'teststring'[-1]` returns `'g'`
- `'teststring'[-9]` returns `'e'`

#### `string[a:c]`
- `'teststring'[0:4]` returns `'test'`
- `'teststring'[4:10]` returns `'string'`

#### `string[a:]`
- `'teststring'[4:]` returns `'string'`
- `'0123456789'[4:]` returns `'456789'`

#### `string[:c]`
- `'teststring'[:4]` returns `'test'`
- `'0123456789'[:4]` returns `'0123'`

#### `string[a:b:c]`
- `'teststring'[0:2:10]` returns `'tssrn'`
- `'0123456789'[0:2:10]` returns `'02468'`
- `'teststring'[1:3:9]` returns `'esi'`
- `'0123456789'[1:3:9]` returns `'147'`
- `'teststring'[1:3:7]` returns `'es'`
- `'0123456789'[1:3:7]` returns `'14'`

#### `string[a:b:]`
- `'teststring'[-1:-1:]` returns `'gnirtstset'`
- `'0123456789'[-1:-1:]` returns `'9876543210'`
- `'teststring'[3:3:]` returns `'trg'`
- `'0123456789'[3:3:]` returns `'369'`

#### `string[:b:c]`
- `'teststring'[:-1:2]` returns `'gnirtst'`
- `'0123456789'[:-1:2]` returns `'9876543'`
- `'teststring'[:2:7]` returns `'tssr'`
- `'0123456789'[:2:7]` returns `'0246'`

#### `string[:b:]`
- `'teststring'[:2:]` returns `'tssrn'`
- `'0123456789'[:2:]` returns `'02468'`
- `'teststring'[:-1:]` returns `'gnirtstset'`
- `'0123456789'[:-1:]` returns `'9876543210'`



**Other Notes**
- `string[:n] + string[n:]` always equals `string`
- Arrays can be passed as indices as well: `s[2,7,8,9]` is equivalent to `s[2]+s[7]+s[8]+s[9]`. These indices need not be in sorted order: `'teststring'[6,7,0,1]` returns `'rite'`
- A useful pattern is to prevent leftwards stepping by providing `b` of `1`. Particularly useful to prevent undesired behavior when `a` and `c` are chosen at runtime.
`'abcde'[1:4]` returns `'bcd'`
`'abcde'[1:1:4]` returns `'bcd'`
`'abcde'[3:0]` returns `'dcb'`
`'abcde'[3:1:0]` returns `''`



- `s = [:4)+[-3:-1]` then `'teststring'[s]` returns `'testing'`
- `'teststring'[2,7,8,9]` returns `'sing'`
'''

'''
harbor: spec/strings/properties
{Properties}[subsection]

- **`.length`** Returns the length of the string
'''

'''
harbor: spec/strings/methods
{Methods}[subsection]

{.escape()}[method] Escapes HTML characters: `'<i>This</i> is an <b>example</b>'.escape()` = `'&lt;i&gt;This&lt;/i&gt; is an &lt;b&gt;example&lt;/b&gt;'`
{.index(sub)}[method] Returns the indices where substring `sub` is found. Returns empty list if not found
{.join(i)}[method] Concatenates the strings in `i`, separated by the given string
{.replace()}[method] Replaces, in-place, certain substrings with supplied substrings. Can be called with a pair of arguments: `.replace(fromSubstring,toSubstring)`. Can also be called with multiple pairs of arguments: `.replace(((from1,to1),(from2,to2)))`. When multiple from/to pairs are provided, they are executed sequentially over the entire string.
{.lower()}[method] Convert all uppercase characters to lowercase
{.upper()}[method] Convert all lowercase characters to uppercase
{.split(sep)}[method] Splits a string into an array of strings, using `sep` as the delimiter.
'''

'''
harbor: spec/strings/url-methods
{URL methods}[subsection]

{.parseurl()}[method] Returns a dictionary containing the URL components, in the following fomat:
```
# 'https://corey:password@www.example.com:8080/dir1/dir2/dir3/text.html?key1=value1&key2=value2#frag'.parseurl()
{'scheme':'https',
 'user':'corey',
 'password':'password',
 'host':'www.example.com',
 'port':8080,
 'path':['dir1','dir2','dir3','text.html'],
 'query':{'key1':'value1',
          'key2':'value2'},
 'fragment':'frag'}
```
```
# 'https://example.com/dir1/dir2/dir3/text.html'.parseurl()
{'scheme':'https',
 'host':'example.com',
 'path':['dir1','dir2','dir3','text.html']}
```

{buildurl(d)}[method] Returns a string built from the provided dictionary. `buildurl(u.parseurl())` will return a URL functionally equivalent to `u`, though it may not be identical.
'''









'''
harbor: spec/dicts
---
{Dictionaries}[section]
'''

'''
harbor: spec/dicts/operations
{Operations}[subsection]
'''

'''
harbor: spec/dicts/operations/creating
{Creating}[subsubsection]

```
height = {'Alice': 5*12 + 8,
          'Bob': 5*12 + 11}

temp = {}
```
'''

'''
harbor: spec/dicts/operations/inserting
{Inserting}[subsubsection]
`height['Eve'] = 5*12 + 9`
'''

'''
harbor: spec/dicts/operations/modifying
{Modifying}[subsubsection]
`height['Bob'] = 6*12`
'''

'''
harbor: spec/dicts/operations/accessing
{Accessing}[subsubsection]
`height['Alice']` Gives error if key not in dictionary
'''

'''
harbor: spec/dicts/operations/deleting
{Deleting}[subsubsection]
`delete height['Alice']`
'''

'''
harbor: spec/dicts/properties
{Properties}[subsection]
'''

'''
harbor: spec/dicts/methods
{Methods}[subsection]

- `k in d` Returns `true` if `k` is a key of `d`
'''








'''
harbor: spec/sets
---

{Sets?}[section]
'''




'''
harbor: spec/types
---
{Types}[section]
'''

'''
harbor: spec/types/operations
{Operations}[subsection]
'''

'''
harbor: spec/types/operations/creating
{Creating}[subsubsection]

`Types` are defined outside of agents:

```
type point:
    float x:
        x >= -180.0
        x <= 180.0

    float y:
        y >= -90.0
        y <= 90.0

define agent1:
    run(i):
        p = point(2.0,3.0)
        p.x -> print
        p -> agent2

define agent2:
    run(point e):
        x,y = e.x,e.y
```

If the `type` is omitted from a subagent definition (`run(point e):`), it defaults to `dict`, which is unrestricted.
The benefits of defining a `type` are essentially in creating a contract between the
developers of each microservice/agent. The variable types of each component can optionally be
specified, and any number of statements may be provided, all of which must evaluate to `true` to
avoid an error. The following doesn't specify variable type:

```
type nonnegative:
    n:
        n >= 0
```

Multiple types can be provided for the same variable, in which case any of them are valid. A component
must obey the statements about its variable type only:

```
type strange:
    float i:
        i < 0

    int i:
        i >= 0
```

Above, `i` can be either a negative `float` or a non-negative integer. Any expression can be
asserted in a `type` definition:

```
type even:
    int i:
        i%2 == 0
```

The following will allow days of the week or `false` value:

```

type day:
    string day:
        day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    bool day:
        day == false

```

Mutually exclusive assertions are possible, even for the same variable type. The following can be an
even integer greater than 5, *or* an odd integer less than or equal to 9:

```
type strange:
    int i:
        i % 2 == 0
        i > 5

    int i:
        i % 2 == 1
        i <= 9
```

This is to prevent monstrosities like the following:

```
# DON'T DO THIS
type awful:
    int i:
        (i % 2 == 0 and i > 5) or (i % 2 == 1 and i <= 9)
```

Assertions involving multiple components are also possible:

```
type tangled:
    int a:
        a >= 0

    int b:
        b >= 0

    :
        (a + b) % 2 == 0
```

Default values are also possible. After the following definition, `example()` will create `{'a':4,'b':0.1}`:
```
type example:
    int a = 4:
        a < 6

    bool a:
        a == false

    float b:
        b < -4.0

    float b = 0.1:
        b >= 0.0
```

Naturally, only one default per component is permissible.

Definitions of `type` will automatically be included in any agents that create them or receive them.
If an agent is sending a defined `type` to another agent who doesn't specify a receiving `type`,
the object will arrive as a simple `dict`, with all fields intact.
'''

'''
harbor: spec/types/properties
{Properties}[subsection]
'''

'''
harbor: spec/types/methods
{Methods}[subsection]
'''





'''
harbor: spec/agents
---

{Agents}[section]
'''

'''
harbor: spec/agents/defining
{Defining}[subsection]

```
define agent:
    subagent:
        # code
```

Defines an agent named `agent`, with one subagent, `subagent`. Valid agent names match this regex: `[a-z][a-zA-Z0-9]*`. Or more verbosely, they consist of a leading lowercase letter, followed by some combination of lowercase letters, uppercase letters, and numerals. Good Swarm style would use `lowerCamelCase`, generally avoiding numerals unless useful for clarity. Underscores are not valid in Swarm agent definitions, and thus `underscored_agent_name` will throw an error.

`print`, `error`, `logging` and `analytics` are illegal agent names, as they would overwrite existing system agents/functions.

`http` is a valid agent name, but only to overload certain methods in the existing agent.
'''

'''
harbor: spec/agents/properties
{Properties}[subsection]

{.name}[method] Returns the name of the agent. Useful as `self.name` (read-only)
{.subagents}[method] Returns the names of all subagents, as an array of strings. (read-only)
'''

'''
harbor: spec/agents/methods
{Methods}[subsection]
'''

'''
harbor: spec/subagents
---

{Subagents}[section]
'''

'''
harbor: spec/subagents/defining
{Defining}[subsection]

A subagent can be modelled as a combination of two things: a `function` and a `queue`. The queue can be appended to by any subagent, including the subagent who owns the queue. As long as there are objects in the queue, the subagent pops objects from it and executes the function with the object as input. Each subagent has its own thread, and can error, crash, and generally operate independently.

To send data to a `queue`, the send command is used: `42 -> average.run`

There are two specially-named subagents:
- `init` is executed once initially, and can set up variables global to all subagents of the agent
- `run` can be referred to via `-> agent.run` or `-> agent`

All subagents except for `init` must take at least one input, while `init` takes none.
'''

'''
harbor: spec/subagents/properties
{Properties}[subsection]

{.queue.length}[method] Returns the current length of the subagent's queue (read-only)
{.queue.first}[method] Returns the object at the front of the queue (ie, next in line to be processed) (read-only)
{.queue.last}[method] Returns the object at the back of the queue (read-only)
{.instances.min}[method] (read/write, non-negative integer)
{.instances.max}[method] (read/write, non-negative integer)
{.instances.desired}[method] (read/write, non-negative integer)
{.instances.current}[method] (read-only, non-negative integer)
'''

'''
harbor: spec/subagents/methods
{Methods}[subsection]

{.queue.popfirst()}[method] Removes and returns the object at the front of the queue (in place)
{.queue.poplast()}[method] Removes and returns the object at the back of the queue (in place)
{.queue.insertfirst()}[method] Inserts an object at the front of the queue
{.queue.insertlast()}[method] Inserts an object at the end of the queue

---
'''






'''
harbor: spec/print

{print}[section]
```
'Strings work' -> print
5 -> print
'Integers work',5 -> print

' ' -> print.separator
for i in [0:5):
    i -> print

'\n' -> print

', ' -> print.separator
for i in [0:5):
    i -> print
0, 1, 2, 3, 4,


```
```
Strings work
5
'Integers work',5
0 1 2 3 4
0, 1, 2, 3, 4,
```
'''

'''
harbor: spec/print/properties
{Properties}[subsection]

{.separator}[method] The string to print after every input. (read/write) Default: `\n`
'''

'''
harbor: spec/print/methods
{Methods}[subsection]
'''





'''
harbor: spec/error
{error}[section]
```
define example:
    init:
        'This is an example error' -> error
```
```
ERROR in 'example.init': This is an example error
```
'''

'''
harbor: spec/error/properties
{Properties}[subsection]

{.levels}[method] A list of the error severity levels, ranked from least to most severe. Default: `['green','yellow','red']` (read/write)
{.ignoreBelow}[method] Sets the severity level below which errors are ignored (read/write) Default: `green`
'''

'''
harbor: spec/error/methods
{Methods}[subsection]
'''





'''
harbor: spec/logging
{logging}[section]
'''

'''
harbor: spec/logging/to-file
{to file}[subsection]
```
define example:
    init:
        'Something happened' -> logging
        'Something else happened' -> logging
        wait(3)
        'And another thing -> logging
```
```
# excerpt of logging text file
1510933165: [2017-11-17 3:39:25 PM GMT] [example.init] Something happened
1510933165: [2017-11-17 3:39:25 PM GMT] [example.init] Something else happened
1510933168: [2017-11-17 3:39:28 PM GMT] [example.init] And another thing
```
'''

'''
harbor: spec/logging/to-screen
{to screen}[subsection}
```
define example:
    init:
        true -> logging.toScreen
        false -> logging.toFile
        'Something happened' -> logging
        'Something else happened' -> logging
        wait(3)
        'And another thing' -> logging
```
```
1510933165: [2017-11-17 3:39:25 PM GMT] [example.init] Something happened
1510933165: [2017-11-17 3:39:25 PM GMT] [example.init] Something else happened
1510933168: [2017-11-17 3:39:28 PM GMT] [example.init] And another thing
```
'''

'''
harbor: spec/logging/properties
{Properties}[subsection]
'''

'''
harbor: spec/logging/methods
{Methods}[subsection]
'''



'''
harbor: spec/analytics
{analytics}[section]

```
define example:
    init:
        'apple' -> analytics
        'pear' -> analytics
        wait(4)
        'apple' -> analytics
        wait(3*60)
        'apple' -> analytics
```
```
# analytics text file
tag: 'apple'
[2017-11-17 3:39:25 - 3:39:30 PM GMT] : 2
[2017-11-17 3:42:25 - 3:42:30 PM GMT] : 1

tag: 'pear'
[2017-11-17 3:39:25 - 3:39:30 PM GMT] : 1
```
(Specification for `analytics` is subject to change)
'''

'''
harbor: spec/analytics/properties
{Properties}[subsection]
'''

'''
harbor: spec/analytics/methods
{Methods}[subsection]
'''








'''
{http}[section]

```
define http:
    receive(req):
        req -> server

define server:
    init:
        ip,'Hello' -> http.send

    run(req):
        'Received something' -> print
```
`http.send` can be sent to, but cannot be user-defined. `http.receive` should be defined in order to route incoming HTTP traffic to various other agents in the program.
'''

'''
harbor: spec/http/properties
{Properties}[subsection]
'''

'''
harbor: spec/http/methods
{Methods}[subsection]
'''

'''
harbor: spec/http/subagents
{Subagents}[subsection]

{.receive}[method] Define to manually handle/route incoming HTTP requests
'''

