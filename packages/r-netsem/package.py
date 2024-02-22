# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetsem(RPackage):
	"""Network Structural Equation Modeling

	The network structural equation modeling conducts a network 
    statistical analysis on a data frame of coincident observations of 
    multiple continuous variables [1]. 
    It builds a pathway model by exploring a pool of domain knowledge guided 
    candidate statistical relationships between each of the variable pairs, 
    selecting the 'best fit' on the basis of a specific criteria such as 
    adjusted r-squared value.
    This material is based upon work supported by the U.S. National Science 
    Foundation Award EEC-2052776 and EEC-2052662 for the MDS-Rely IUCRC Center, 
    under the NSF Solicitation: 
    NSF 20-570 Industry-University Cooperative Research Centers Program 
    [1] Bruckman, Laura S., Nicholas R. Wheeler, Junheng Ma, Ethan Wang, 
    Carl K. Wang, Ivan Chou, Jiayang Sun, and Roger H. French. (2013) 
    <doi:10.1109/ACCESS.2013.2267611>.
	"""
	
	cran = "netSEM" 

	version("0.6.2", md5="82cd4d3345e90c5f6e89ab14cde357ac")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-diagrammer@0.9.2:", type=("build", "run"))
	depends_on("r-diagrammersvg@0.1:", type=("build", "run"))
	depends_on("r-htmlwidgets@1.2:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
	depends_on("r-rsvg@1.1:", type=("build", "run"))
	depends_on("r-svglite@1.2.1:", type=("build", "run"))
	depends_on("r-png@0.1.7:", type=("build", "run"))
	depends_on("r-segmented@0.5.3:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
