# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbi(RPackage):
	"""Interface to 'LibBi'

	Provides a complete interface to 'LibBi', a library for Bayesian
    inference (see <https://libbi.org> and Murray, 2015
    <doi:10.18637/jss.v067.i10> for more information). This includes functions
    for manipulating 'LibBi' models, for reading and writing 'LibBi'
    input/output files, for converting 'LibBi' output to provide traces for use
    with the coda package, and for running 'LibBi' to conduct inference.
	"""
	
	homepage = "https://github.com/sbfnk/rbi"
	cran = "rbi" 

	version("1.0.0", md5="4c79710e27ae16f61149ded96d331063")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
