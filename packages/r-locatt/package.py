# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocatt(RPackage):
	"""Geographically-Conscious Taxonomic Assignment for Metabarcoding

	A bioinformatics pipeline for performing taxonomic
    assignment of DNA metabarcoding sequence data while considering
    geographic location. A detailed tutorial is available at
    <https://urodelan.github.io/Local_Taxa_Tool_Tutorial/>.
    A manuscript describing these methods is in preparation.
	"""
	
	homepage = "https://github.com/Urodelan/LocaTT"
	cran = "LocaTT" 

	version("1.1.1", md5="ed92cb0bea6375b25455c73ad1c2b89e")

	depends_on("r-taxize", type=("build", "run"))
