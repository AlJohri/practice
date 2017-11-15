"""
Flatten a Dictionary

A dictionary is a type of data structure that is supported natively in
all major interpreted languages such as JavaScript, Python, Ruby and PHP,
where it’s known as an Object, Dictionary, Hash and Array, respectively.
In simple terms, a dictionary is a collection of unique keys and their
values. The values can typically be of any primitive type (i.e an integer,
boolean, double, string etc) or other dictionaries (dictionaries can be
nested). However, for this exercise assume that values are either an
integer, a string or another dictionary.

Given a dictionary dict, write a function flattenDictionary that returns
a flattened version of it .

If you’re using a compiled language such Java, C++, C#, Swift and Go,
you may want to use a Map/Dictionary/Hash Table that maps strings (keys)
to a generic type (e.g. Object in Java, AnyObject in Swift etc.) to
allow nested dictionaries.

Example:

input:  dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : "1"
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
        }


Important: when you concatenate keys, make sure to add the dot character
between them. For instance concatenating Key2, c and d the result key
would be Key2.c.d.

Tips:

If your peer cannot come up with a solution, ask them to analyze the
input and see if they see a pattern.

If still no progress, try to direct them toward a recursive approach.

If your peer makes some progress with the recursive approach, and is
stuck at some other point, try to give some hints regarding how keys
of the dictionary could be manipulated.

Watch out of cases when the key is an empty string or null. For
instance, the input dictionary itself isn’t associated with any key. In that
"""

def flatten_dictionary(d, parent=""):
  for key in list(d.keys()):
    value = d.pop(key)

    if parent and key:
      new_key = parent + "." + key
    else:
      new_key = key or parent or ""

    if isinstance(value, str) or isinstance(value, int):
      d[new_key] = value
    else:
      flattened_d = flatten_dictionary(value, new_key)
      d.update(flattened_d)

  return d


tests = [
  {
    "input": {"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":"1"}}},
    "expected": {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e":"1"}
  },
  {
    "input": {"Key":{"a":"2","b":"3"}},
    "expected": {"Key.a":"2","Key.b":"3"},
  },
  {
    "input": {"Key1":"1","Key2":{"a":"2","b":"3","c":{"d":"3","e":{"f":"4"}}}},
    "expected": {"Key1":"1","Key2.a":"2","Key2.b":"3","Key2.c.d":"3","Key2.c.e.f":"4"},
  },
  {
    "input": {"":{"a":"1"},"b":"3"},
    "expected": {"a":"1","b":"3"},
  },
  {
    "input": {"a":{"b":{"c":{"d":{"e":{"f":{"":"pramp"}}}}}}},
    "expected": {"a.b.c.d.e.f":"pramp"}
  },
  {
    "input": {"a":"1"},
    "expected": {"a":"1"}
  }
]

for i, test in enumerate(tests):
  print(f"Test Case {i}")
  print("Input", test['input'])
  print("Expected", test['expected'])
  actual = flatten_dictionary(test['input'])
  print("Actual", actual)
  if actual == test['expected']:
    print("Passed")
  else:
    print("Failed")
  print()

"""
Solution

Recursion is natural choice for this kind of problem. We iterate over
the keys in dict and distinguish between two cases: If the value mapped
to a key is a primitive, we take that key and simply concatenate it to
the flattened key we created up to this point. We then map the resultant
key to the value in the output dictionary. If the value is a dictionary,
we do the same concatenation, but instead of mapping the result to the
value in the output dictionary, we recurse on the value with the newly
formed key.

Pseudocode:

function flattenDictionary(dict):
    flatDictionary = {}
    flattenDictionaryHelper("", dict, flatDictionary)

    return flatDictionary


function flattenDictionaryHelper(initialKey, dict, flatDictionary):
    for (key : dict.keyset()):
        value = dict.get(key)

        if (!isDictionary(value)): # the value is of a primitive type
            if (initialKey == null || initialKey == ""):
                flatDictionary.put(key, value)
            else:
                flatDictionary.put(initialKey + "." + key, value)
        else:
            if (initialKey == null || initialKey == "")
                flattenDictionaryHelper(key, value, flatDictionary)
            else:
                flattenDictionaryHelper(initialKey + "." + key, value, flatDictionary)

Time Complexity: O(N), where N is the number of keys in the input dictionary.
We visit every key in dictionary only once, hence the linear time complexity.

Space Complexity: O(N) since the output dictionary is asymptotically as big
as the input dictionary. We also store recursive calls in the execution
stack which in the worst case scenario could be O(N), as well. The total
is still O(N).
"""