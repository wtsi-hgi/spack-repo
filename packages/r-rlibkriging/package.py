# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlibkriging(RPackage):
	"""Kriging Models using the 'libKriging' Library

	Interface to 'libKriging' 'C++' library <https://github.com/libKriging> that should
    provide most standard Kriging / Gaussian process regression features
    (like in 'DiceKriging', 'kergp' or 'RobustGaSP' packages).
    'libKriging' relies on Armadillo linear algebra library (Apache 2 license) by Conrad Sanderson, 
    'lbfgsb_cpp' is a 'C++' port around 'lbfgsb' library (BSD-3 license) by 
    Ciyou Zhu, Richard Byrd, Jorge Nocedal and Jose Luis Morales used for hyperparameters optimization,
    and HDF5 features coming from HDF Group (see HDF5_LICENSE file)
    possibly provided by Rhdf5lib by Mike Smith (Artistic-2.0 license).
	"""
	
	homepage = "https://github.com/libKriging"
	cran = "rlibkriging" 

	version("0.8-0.1", md5="ace0e4a57d806b73535ccb1657167ce5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("cmake@3.2.0:", type=("build", "link", "run"))
	depends_on("gcc", type=("build", "link", "run"))
	depends_on("gfortran", type=("build", "link", "run"))
	depends_on("hdf5", type=("build", "link", "run"))
