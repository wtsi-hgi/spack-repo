# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTr8(RPackage):
	"""A Tool for Downloading Functional Traits Data for Plant Species

	Plant ecologists often need to collect "traits" data
    about plant species which are often scattered among various
    databases: TR8 contains a set of tools which take care of
    automatically retrieving some of those functional traits data
    for plant species from publicly available databases (Biolflor,
    The Ecological Flora of the British Isles, LEDA traitbase, Ellenberg
    values for Italian Flora, Mycorrhizal intensity databases, Catminat, BROT,
    PLANTS, Jepson Flora Project).
    The TR8 name, inspired by "car plates" jokes, was chosen since
    it both reminds of the main object of the package and is
    extremely short to type.
	"""
	
	homepage = "https://github.com/GioBo/TR8"
	cran = "TR8" 

	version("0.9.22", md5="9bcc6bfe3e0f4a52e285d95541602a7f", url="https://cran.r-project.org/src/contrib/TR8_0.9.22.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
