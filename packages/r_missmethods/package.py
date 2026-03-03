# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMissmethods(RPackage):
	"""Methods for Missing Data

	Supply functions for the creation and handling of missing
    data as well as tools to evaluate missing data methods. Nearly all
    possibilities of generating missing data discussed by Santos et al.
    (2019) <doi:10.1109/ACCESS.2019.2891360> and some additional are
    implemented.  Functions are supplied to compare parameter estimates
    and imputed values to true values to evaluate missing data methods.
    Evaluations of these types are done, for example, by Cetin-Berber et
    al. (2019) <doi:10.1177/0013164418805532> and Kim et al. (2005)
    <doi:10.1093/bioinformatics/bth499>.
	"""
	
	homepage = "https://github.com/torockel/missMethods"
	cran = "missMethods" 

	version("0.4.0", md5="0e3a8e72e6a1c681b47d944542d3b1db")

	depends_on("r-mvtnorm", type=("build", "run"))
