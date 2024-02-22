# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlca(RPackage):
	"""An R Package for Multiple-Group Latent Class Analysis

	Fits multiple-group latent class analysis (LCA) for exploring 
    differences between populations in the data with a multilevel structure. 
    There are two approaches to reflect group differences in glca: 
    fixed-effect LCA (Bandeen-Roche et al (1997) <doi:10.1080/01621459.1997.10473658>;
    Clogg and Goodman (1985) <doi:10.2307/270847>) and nonparametric random-effect LCA 
    (Vermunt (2003) <doi:10.1111/j.0081-1750.2003.t01-1-00131.x>).
	"""
	
	homepage = "https://kim0sun.github.io/glca/"
	cran = "glca" 

	version("1.4.0", md5="cc34f268be675b2ba11ce3bc61647fa3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
