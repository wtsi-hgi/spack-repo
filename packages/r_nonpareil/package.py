# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonpareil(RPackage):
	"""Metagenome Coverage Estimation and Projections for 'Nonpareil'

	Plot, process, and analyze NPO files produced by
    'Nonpareil' <http://enve-omics.ce.gatech.edu/nonpareil/>.
	"""
	
	homepage = "http://enve-omics.ce.gatech.edu/nonpareil/"
	cran = "Nonpareil" 

	version("3.4.0", md5="e4d80621eb9ac4e8979c7689cc8e59f3")

	depends_on("r@2.9:", type=("build", "run"))
