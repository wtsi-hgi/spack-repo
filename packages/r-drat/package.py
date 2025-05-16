# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrat(RPackage):
	"""'Drat' R Archive Template

	Creation and use of R Repositories via helper functions 
 to insert packages into a repository, and to add repository information 
 to the current R session. Two primary types of repositories are support:
 gh-pages at GitHub, as well as local repositories on either the same machine
 or a local network. Drat is a recursive acronym: Drat R Archive Template. 
	"""
	
	homepage = "https://github.com/eddelbuettel/drat"
	cran = "drat" 

	version("0.2.4", md5="e46a40f8f72625d1e0a590d022603117")
	version("0.2.3", md5="189ddcfa0554f351be2bf15fb1c61f82")

	depends_on("r@3.6:", type=("build", "run"))
