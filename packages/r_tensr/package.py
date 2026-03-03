# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensr(RPackage):
	"""Covariance Inference and Decompositions for Tensor Datasets

	A collection of functions for Kronecker structured covariance
    estimation and testing under the array normal model. For estimation,
    maximum likelihood and Bayesian equivariant estimation procedures are
    implemented. For testing, a likelihood ratio testing procedure is
    available. This package also contains additional functions for manipulating
    and decomposing tensor data sets. This work was partially supported by NSF
    grant DMS-1505136. Details of the methods are described in
    Gerard and Hoff (2015) <doi:10.1016/j.jmva.2015.01.020> and
    Gerard and Hoff (2016) <doi:10.1016/j.laa.2016.04.033>.
	"""
	
	cran = "tensr" 

	version("1.0.1", md5="7ce35af154fac404c1da6bed60f1e899")

	depends_on("r-assertthat", type=("build", "run"))
