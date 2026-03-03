# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlocklength(RPackage):
	"""Select an Optimal Block-Length to Bootstrap Dependent Data
(Block Bootstrap)

	A set of functions to select the optimal block-length for a 
    dependent bootstrap (block-bootstrap). Includes the Hall, Horowitz, and Jing
    (1995) <doi:10.1093/biomet/82.3.561> cross-validation method and the 
    Politis and White (2004) <doi:10.1081/ETC-120028836> Spectral Density 
    Plug-in method, including the Patton, Politis, and White (2009)
    <doi:10.1080/07474930802459016> correction with a corresponding set of S3
    plot methods.
	"""
	
	homepage = "https://alecstashevsky.com/r/blocklength"
	cran = "blocklength" 

	version("0.1.5", md5="296c9ca3bb0bd3078727bffec669e849")

	depends_on("r-tseries", type=("build", "run"))
