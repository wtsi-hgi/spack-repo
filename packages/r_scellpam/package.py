# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScellpam(RPackage):
	"""Applying Partitioning Around Medoids to Single Cell Data with
High Number of Cells

	PAM (Partitioning Around Medoids) algorithm application to samples of single cell sequencing techniques
	     with a high number of cells (as many as the computer memory allows). The package uses a binary format to
	     store matrices (either full, sparse or symmetric) in files written in the disk that can contain any data type
	     (not just double) which allows its manipulation when memory is sufficient to load them as int or float, but not
	     as double. The PAM implementation is done in parallel, using several/all the cores of the machine, if it has them.
	     This package shares a great part of its code with packages 'jmatrix' and 'parallelpam' but their functionality is
	     included here so there is no need to install them.
	"""
	
	cran = "scellpam" 

	version("1.4.5", md5="53ee47438d3d67249bf7638feed309c3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-memuse@4.2.1:", type=("build", "run"))
	depends_on("r-cluster@2.1.4:", type=("build", "run"))
