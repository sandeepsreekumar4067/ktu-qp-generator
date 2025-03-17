from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API = os.getenv("GEMINI_API")
client = genai.Client(api_key=GEMINI_API)

papper_1 ="""

**Sample Question Paper 1:**

*Course Code:* EST100  
*Course Name:* Engineering Mechanics  
*Examination:* December 2023

**Part A: (Answer all questions, each carries 3 marks.)**

1. A ladder weighing 30 kg is supported at a wall and floor. A man weighing 72 kg stands on it vertically, 8 m above the floor level. There is a 100 kg force acting at the top-most point of the ladder vertically. Considering all contact surfaces smooth, draw the free body diagram.

2. State and explain Varignon’s theorem for concurrent coplanar forces.

3. Briefly explain the analysis of forces acting on a wedge with a suitable example.

4. A simply supported beam AB of span 4 m is carrying point loads of 10 N, 6 N, and 4 N at 1 m, 2 m, and 3 m respectively from support A. Calculate the reactions at supports A and B.

5. A force \( \mathbf{F} = 2\mathbf{i} + 4\mathbf{j} - 3\mathbf{k} \) is applied at the point A(1,1,-2). Determine the moment of the force about the origin.

**Part B: (Answer any two full questions from each set, each carries 10 marks.)**

*Set I:*

6. Three spheres A, B, and C weighing 300 N, 600 N, and 300 N respectively and having diameters 800 mm, 1200 mm, and 800 mm respectively are placed in a trench inclined at 30°. Determine the reactions developed at contact points.

7. Determine the resultant of the three forces acting on a dam section and locate its intersection with the base. For a safe design, this intersection should be within the middle third. Is it a safe design?

*Set II:*

8. A block weighing 500 N is resting on a rough horizontal surface with a coefficient of friction of 0.3. Determine the minimum force required to start moving the block.

9. A particle moves along a straight line with an acceleration given by \( a = 5 - 2v \), where \( v \) is the velocity at any time \( t \). If the initial velocity is zero, find the velocity as a function of time.

*Set III:*

10. A simply supported beam of length 6 m carries a uniformly distributed load of 2 kN/m over its entire length. Calculate the maximum bending moment and the position where it occurs.
"""

papper_2 = """

**Sample Question Paper 2:**

*Course Code:* BE100  
*Course Name:* Engineering Mechanics  
*Examination:* July 2018

**Part A: (Answer all questions, each carries 5 marks.)**

1. Differentiate between the various types of supports for beams.

2. Explain Free Body Diagram with sketches.

3. What are the characteristics of dry friction?

4. Differentiate between ‘polar moment of inertia’ and ‘product of inertia’.

5. Define the term instantaneous centre in plane motion and explain the methods to locate it.

**Part B: (Answer any two full questions from each set, each carries 10 marks.)**

*Set I:*

6. Three spheres A, B, and C weighing 300 N, 600 N, and 300 N respectively and having diameters 800 mm, 1200 mm, and 800 mm respectively are placed in a trench inclined at 30°. Determine the reactions developed at contact points P, Q, R, and S.

7. Determine the resultant of the three forces acting on the dam section shown and locate its intersection with the base AB. For a safe design, this intersection should be within the middle third. Is it a safe design?

*Set II:*

8. A block weighing 500 N is resting on a rough horizontal surface with a coefficient of friction of 0.3. Determine the minimum force required to start moving the block.

9. A particle moves along a straight line with an acceleration given by \( a = 5 - 2v \), where \( v \) is the velocity at any time \( t \). If the initial velocity is zero, find the velocity as a function of time.

*Set III:*

10. A simply supported beam of length 6 m carries a uniformly distributed load of 2 kN/m over its entire length. Calculate the maximum bending moment and the position where it occurs.


"""



papper_3 = """

**Sample Question Paper 3:**

*Course Code:* EST100  
*Course Name:* Engineering Mechanics  
*Examination:* January 2021

**Part A: (Answer all questions, each carries 5 marks.)**

1. Define the term 'centroid' and explain its significance in engineering mechanics.

2. Explain the concept of 'moment of inertia' and its application in structural engineering.

3. Describe the different types of equilibrium conditions for a rigid body.

4. What is the principle of virtual work? Provide an example of its application.

5. Explain the difference between kinematics and kinetics in the study of dynamics.

**Part B: (Answer any two full questions from each set, each carries 10 marks.)**

*Set I:*

6. A uniform rod of length 5 m and weight 200 N is hinged at one end and held in a horizontal position by a rope attached to the other end. The rope makes an angle of 30° with the horizontal. Determine the tension in the rope and the reaction at the hinge.

7. A block of mass 50 kg rests on an inclined plane making an angle of 20° with the horizontal. The coefficient of static friction between the block and the plane is 0.25. Determine whether the block will slide down the plane. 

"""

sample_pappers = f"Papper 1:{papper_1}\n\n Papper 2 : {papper_2} \n\n Papper3 : {papper_3} "


prompt = f"""
    You are an expert in Engineering Mechanics and an AI exam paper generator. 
    Given the following sample question papers, generate a new high-quality question paper following the given format.
    
    **Sample Papers:**
    {sample_pappers}
    **Now, generate a fresh question paper using the format of pappers given**


    Ensure the questions are original, follow the same complexity, and cover diverse topics.
"""


response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0.1
    )
)
print(response.text)