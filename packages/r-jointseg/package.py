# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointseg(RPackage):
	"""Joint Segmentation of Multivariate (Copy Number) Signals

	Methods for fast segmentation of multivariate
    signals into piecewise constant profiles and for generating realistic
    copy-number profiles. A typical application is the joint segmentation of total
    DNA copy numbers and allelic ratios obtained from Single Nucleotide Polymorphism
    (SNP) microarrays in cancer studies. The methods are described in Pierre-Jean, 
    Rigaill and Neuvial (2015) <doi:10.1093/bib/bbu026>.
	"""
	
	homepage = "https://github.com/mpierrejean/jointseg"
	cran = "jointseg" 

	version("1.0.2", md5="b88db34f0bc0b350f565cd82fc82d807")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-acnr@0.3.1:", type=("build", "run"))
	depends_on("r-matrixstats@0.6:", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
