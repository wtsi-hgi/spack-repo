# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFiberld(RPackage):
	"""Fiber Length Determination

	Routines for estimating tree fiber (tracheid) length distributions in the standing tree
           based on increment core samples. Two types of data can be used with the package, increment 
           core data measured by means of an optical fiber analyzer (OFA), e.g. such as the Kajaani 
          Fiber Lab, or measured by microscopy. Increment core data analyzed by OFAs consist of the cell
          lengths of both cut and uncut fibres (tracheids) and fines (such as ray parenchyma cells)
           without being able to identify which cells are cut or if they are fines or fibres. The
          microscopy measured data consist of the observed lengths of the uncut fibres in the increment
         core. A censored version of a mixture of the fine and fiber length distributions is proposed to
         fit the OFA data, under distributional assumptions (Svensson et al., 2006) <doi:10.1111/j.1467-9469.2006.00501.x>. The package offers two choices for the
        assumptions of the underlying density functions of the true fiber (fine) lenghts of those fibers
        (fines) that at least partially appear in the increment core, being the generalized gamma and 
        the log normal densities.
	"""
	
	cran = "fiberLD" 

	version("0.1-8", md5="a8ea42d858673de74a4f6c5896d29a5b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
