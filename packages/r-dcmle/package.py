# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcmle(RPackage):
	"""Hierarchical Models Made Easy with Data Cloning

	S4 classes around infrastructure provided by the
    'coda' and 'dclone' packages to make package development easy as a breeze
    with data cloning for hierarchical models.
	"""
	
	homepage = "https://groups.google.com/forum/#!forum/dclone-users"
	cran = "dcmle" 

	version("0.4-1", md5="8e9468e2971e673a3c9c1ce614f5bf07")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-dclone@2.0.0:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("jags@3.0.0:", type=("build", "link", "run"))
