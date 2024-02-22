# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRzooroh(RPackage):
	"""Partitioning of Individual Autozygosity into Multiple
Homozygous-by-Descent Classes

	Functions to identify Homozygous-by-Descent (HBD) segments associated with runs of homozygosity (ROH) and to
    estimate individual autozygosity (or inbreeding coefficient). HBD segments and autozygosity are assigned to multiple HBD classes
    with a model-based approach relying on a mixture of exponential distributions. The rate of the exponential distribution is distinct
    for each HBD class and defines the expected length of the HBD segments. These HBD classes are therefore related to the age of the
    segments (longer segments and smaller rates for recent autozygosity / recent common ancestor). The functions allow to estimate the
    parameters of the model (rates of the exponential distributions, mixing proportions), to estimate global and local autozygosity
    probabilities and to identify HBD segments with the Viterbi decoding. The method is fully described in Druet and Gautier (2017)
    <doi:10.1111/mec.14324>. 
	"""
	
	cran = "RZooRoH" 

	version("0.3.2.1", md5="254547463da901d78e36d7a9247137b3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
