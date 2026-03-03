# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpreval(RPackage):
	"""Evaluation of Sprinkler Irrigation Uniformity and Efficiency

	Processing and analysis of field collected or simulated sprinkler 
    system catch data (depths) to characterize irrigation uniformity and efficiency using
    standard and other measures. Standard measures include the Christiansen coefficient
    of uniformity (CU) as found in Christiansen, J.E.(1942, ISBN:0138779295,
    "Irrigation by Sprinkling"); and distribution uniformity (DU), potential
    efficiency of the low quarter (PELQ), and application efficiency of the low quarter (AELQ)
    that are implementations of measures of the same notation in Keller, J. and Merriam, 
    J.L. (1978) "Farm Irrigation System Evaluation: A Guide for Management"
    <https://pdf.usaid.gov/pdf_docs/PNAAG745.pdf>. spreval::DU.lh is similar to spreval::DU
    but is the distribution uniformity of the low half instead of low quarter as in DU.
    spreval::PELQT is a version of spreval::PELQ adapted for traveling systems instead
    of lateral move or solid-set sprinkler systems. The function spreval::eff is
    analogous to the method used to compute application efficiency for furrow irrigation
    presented in Walker, W. and Skogerboe, G.V. (1987,ISBN:0138779295, "Surface
    Irrigation: Theory and Practice"),that uses piecewise integration of infiltrated
    depth compared against soil-moisture deficit (SMD), when the argument "target"
    is set equal to SMD.  The other functions contained in the package provide 
    graphical representation of sprinkler system uniformity, and other standard
    univariate parametric and non-parametric statistical measures as applied to
    sprinkler system catch depths. A sample data set of field test data spreval::catchcan
    (catch depths) is provided and is used in examples and vignettes. Agricultural systems
    emphasized, but this package can be used for landscape irrigation evaluation, and a
    landscape (turf) vignette is included as an example application.
	"""
	
	homepage = "https://glgrabow.github.io/spreval/"
	cran = "spreval" 

	version("1.1.0", md5="562adbdb13e72260fc2da5eb8d7f6bda")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
