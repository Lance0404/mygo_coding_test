class UnmatchException(Exception):
  pass

class TestException(Exception):
  pass

def reverse_dict(input: dict) -> dict:
  output = {}
  items = []
  if not isinstance(input, dict):
    raise UnmatchException("unmatched type, expected dict")

  tmp = input
  while hasattr(tmp, 'keys'):      
    k = list(tmp.keys())[0]
    items.append(k)
    tmp = tmp[k]
  items.append(tmp)

  # print(f'items {items}')

  tmp_2 = output
  while len(items) > 2:
    i = items.pop()
    tmp_2.setdefault(i, {})
    tmp_2 = tmp_2[i]
  i = items.pop()
  tmp_2[i] = items.pop()
  
  return output


# Input:
input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}

# Output:
output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}

if __name__ == "__main__":
  acutual_output_value = reverse_dict(input_value)
  print(acutual_output_value)
