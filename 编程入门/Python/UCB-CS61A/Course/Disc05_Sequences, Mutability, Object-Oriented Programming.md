# Mutability

`s1[:3] is s2[:3]`
> Slicing creates new Objects

`s1[4].append(2) 
`s3[6][3]`
> Shallow copy of nested list refers to the same list

```python
if __name__ == "__main__":
    s1 = [1, 2, 3]
    s2 = s1
    print(f"s1iss2:\t{s1 is s2}")
    s2.extend([5, 6])
    print(f"s1[4]:\t{s1[4]}")
    s1.append([-1, 0, 1])
    print(f"s2[5]:\t{s2[5]}")
    s3 = s2[:]
    print(f"s3:\t{s3}")
    s3.insert(3, s2.pop(3))
    print(f"len(s1):\t{len(s1)}")
    print(f"s1[4] is s3[6]:\t{s1[4] is s3[6]}")
    print(f"s3[s2[4][1]]:\t{s3[s2[4][1]]}")
    print(f"s1[:3] is s2[:3]:\t{s1[:3] is s2[:3]}")
    print(f"s1[:3] == s2[:3]:\t{s1[:3] == s2[:3]}")
    s1[4].append(2)
    print(f"s3[6][3]:\t{s3[6][3]}")
```


