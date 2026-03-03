# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REuclideansd(RPackage):
	"""An Euclidean View of Center and Spread

	Illustrates the concepts developed in Sarkar and Rashid (2019, ISSN:0025-5742) <http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiH4deL3q3xAhWX73MBHR_wDaYQFnoECAUQAw&url=https%3A%2F%2Fwww.indianmathsociety.org.in%2Fmathstudent-part-2-2019.pdf&usg=AOvVaw3SY--3T6UAWUnH5-Nj6bSc>.
  This package helps a user guess four things (mean, MD, scaled MSD, and RMSD) before they get the SD. 
    1) The package displays the Empirical Cumulative Distribution Function (ECDF) of
  the given data. The user must choose the value of the mean by equating the areas of 
  two colored (blue and green) regions. The package gives feedback to improve the choice
  until it is correct. Alternatively, the reader may continue with a different guess for 
  the center (not necessarily the mean).
    2) The user chooses the values of the Mean Deviation (MD) based on the ECDF of the deviations
  by equating the areas of two newly colored (blue and green) regions, with feedback from the 
  package until the user guesses correctly.
    3) The user chooses the Scaled Mean Squared Deviation (MSD) based on the ECDF of the scaled 
  square deviations by equating the areas of two newly colored (blue and green) regions, with 
  feedback from the package until the user guesses correctly.
    4) The user chooses the Root Mean Squared Deviation (RMSD) by ensuring that its intersection 
  with the ECDF of the deviations is at the same height as the intersection between the scaled 
  MSD and the ECDF of the scaled squared deviations. Additionally, the intersection of two
  blue lines (the green dot) should fall on the vertical line at the maximum deviation. 
    5) Finally, if the mean is chosen correctly, only then the user can view the population 
  SD (the same as the RMSD) and the sample SD (sqrt(n/(n-1))*RMSD) by clicking the respective 
  buttons. If the mean is chosen incorrectly, the user is asked to correct it. 
	"""
	
	cran = "EuclideanSD" 

	version("0.1.0", md5="2ead48affc7aa7f02429775b414128fd")

	depends_on("r-shiny", type=("build", "run"))
