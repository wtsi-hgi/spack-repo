# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellvolumedist(RPackage):
	"""Functions to Fit Cell Volume Distributions and Thereby Estimate
Cell Growth Rates and Division Times

	Implements a methodology for using cell volume
        distributions to estimate cell growth rates and division times
        that is described in the paper entitled, "Cell Volume
        Distributions Reveal Cell Growth Rates and Division Times", by
        Michael Halter, John T. Elliott, Joseph B. Hubbard, Alessandro
        Tona and Anne L. Plant, which is in press in the Journal of
        Theoretical Biology.  In order to reproduce the analysis used
        to obtain Table 1 in the paper, execute the command
        "example(fitVolDist)".
	"""
	
	cran = "cellVolumeDist" 

	version("1.4", md5="db749627e2a60593fcdae435c4179e33")

	depends_on("r-minpack-lm@1.1.1:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
