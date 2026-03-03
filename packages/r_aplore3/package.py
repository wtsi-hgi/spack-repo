# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAplore3(RPackage):
	"""Datasets from Hosmer, Lemeshow and Sturdivant, "Applied Logistic
Regression" (3rd Ed., 2013)

	An unofficial companion to "Applied
    Logistic Regression" by D.W. Hosmer, S. Lemeshow and
    R.X. Sturdivant (3rd ed., 2013) containing the dataset used in the book.
	"""
	
	homepage = "https://github.com/lbraglia/aplore3"
	cran = "aplore3" 

	version("0.9", md5="21812a5e3837d10d46cd32f5e0333ddf", url="https://cran.r-project.org/src/contrib/aplore3_0.9.tar.gz")

	depends_on("r@3.1.1:", type=("build", "run"))
