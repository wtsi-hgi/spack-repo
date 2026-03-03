# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSepkoski(RPackage):
	"""Sepkoski's Fossil Marine Animal Genera Compendium

	Stratigraphic ranges of fossil marine animal genera from Sepkoski's
    (2002) published compendium. No changes have been made to any taxonomic 
    names. However, first and last appearance intervals have been updated to be
    consistent with stages of the International Geological Timescale. 
    Functionality for generating a plot of Sepkoski's evolutionary fauna is also
    included. For specific details on the compendium see:
    Sepkoski, J. J. (2002). A compendium of fossil marine animal genera.
    Bulletins of American Paleontology, 363, pp. 1–560 (ISBN 0-87710-450-6).
    Access: <https://www.biodiversitylibrary.org/item/40634#page/5/mode/1up>.
	"""
	
	homepage = "https://github.com/LewisAJones/sepkoski"
	cran = "sepkoski" 

	version("0.0.1", md5="e90c4a354c09f3a84af7dc1e544241c2")

	depends_on("r@3.5:", type=("build", "run"))
