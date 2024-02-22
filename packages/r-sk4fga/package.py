# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSk4fga(RPackage):
	"""Scott-Knott for Forensic Glass Analysis

	In forensics, it is common and effective practice to analyse glass fragments from the scene and suspects 
  to gain evidence of placing a suspect at the crime scene. 
  This kind of analysis involves comparing the physical and chemical attributes of glass fragments that exist on both the 
  person and at the crime scene, and assessing the significance in a likeness that they share. 
  The package implements the Scott-Knott Modification 2 algorithm (SKM2) (Christopher M. Triggs and 
  James M. Curran and John S. Buckleton and Kevan A.J. Walsh (1997) <doi:10.1016/S0379-0738(96)02037-3> 
  "The grouping problem in forensic glass analysis: a divisive approach", Forensic Science International, 85(1), 1--14)
  for small sample glass fragment analysis using the refractive index (ri) of a set of glass samples. 
  It also includes an experimental multivariate analog to the Scott-Knott algorithm for similar analysis on glass samples
  with multiple chemical concentration variables and multiple samples of the same item; testing against the Hotellings T^2 
  distribution (J.M. Curran and C.M. Triggs and J.R. Almirall and J.S. Buckleton and K.A.J. Walsh (1997) 
  <doi:10.1016/S1355-0306(97)72197-X> "The interpretation of elemental composition measurements from forensic 
  glass evidence", Science & Justice, 37(4), 241--244).
	"""
	
	homepage = "https://github.com/tobyhayward13/SCI118UOA_ForensicGlassAnalysis"
	cran = "SK4FGA" 

	version("0.1.1", md5="6daea3144621bc6b3c9783ba153a3fe8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
