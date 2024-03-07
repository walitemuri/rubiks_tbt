# Desired outcome: array of all moves required to solve the cube

# Input: Scrambled cube

# Beginners method
"""

"""
cube = {
    
    "U": [["W", "W"], 
          ["W", "W"]],
    
    "F": [["G", "G"], 
          ["G", "G"]],
    
    "R": [["O", "O"],         
          ["O", "O"]],
    
    "D": [["Y", "Y"], 
          ["Y", "Y"]],
    
    "L": [["R", "R"], 
          ["R", "R"]],
    
    "B": [["B", "B"], 
          ["B", "B"]]
}


def rotate_face(face):
  """Rotate a face 90 degrees clockwise."""
  return [[face[1][0], face[0][0]], [face[1][1], face[0][1]]]


def turn_right():
  # Rotate the right face itself
  cube["R"] = rotate_face(cube["R"])

  # Temporarily store the stickers from the up (U) face
  temp = [cube["U"][0][1], cube["U"][1][1]]

  # Move stickers from the front (F) face to the up (U) face
  cube["U"][0][1], cube["U"][1][1] = cube["F"][0][1], cube["F"][1][1]

  # Move stickers from the down (D) face to the front (F) face
  cube["F"][0][1], cube["F"][1][1] = cube["D"][0][1], cube["D"][1][1]

  # The back face movements are inverted because the back face is oriented opposite to the front.
  cube["D"][0][1], cube["D"][1][1] = cube["B"][1][0], cube["B"][0][0]

  # Move the temporarily stored stickers to the back (B) face
  cube["B"][0][0], cube["B"][1][0] = temp[1], temp[
      0]  # Note the order and positions are adjusted for correct orientation

  return


def rotate_face_counter(face):
  """Rotate a face 90 degrees counterclockwise."""
  return [[face[0][1], face[1][1]], [face[0][0], face[1][0]]]


def turn_right_inverted():
  # Rotate the right face counterclockwise
  cube["R"] = rotate_face_counter(cube["R"])

  # Temporarily store the stickers from the up (U) face
  temp = [cube["U"][0][1], cube["U"][1][1]]

  # Move stickers from the back (B) face to the up (U) face
  cube["U"][0][1], cube["U"][1][1] = cube["B"][1][0], cube["B"][0][0]

  # Move stickers from the down (D) face to the back (B) face
  cube["B"][0][0], cube["B"][1][0] = cube["D"][1][1], cube["D"][0][1]

  # Move stickers from the front (F) face to the down (D) face
  cube["D"][0][1], cube["D"][1][1] = cube["F"][0][1], cube["F"][1][1]

  # Move the temporarily stored stickers to the front (F) face
  cube["F"][0][1], cube["F"][1][1] = temp[0], temp[1]

  return


def turn_left_inverted():
  return


def turn_left():
  return


def turn_up():
  return


def turn_up_inverted():
  return


def turn_forward():
  return


def turn_forward_inverted():
  return


def turn_down():
  return


def turn_down_inverted():
  return


def turn_back():
  return


def turn_back_inverted():
  return


def solve_cube():
  return


def main():
  print(cube["U"])


turn_right_inverted()
main()
