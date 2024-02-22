# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapport(RPackage):
	"""A Report Templating System

	Facilitating the creation of reproducible statistical
    report templates. Once created, rapport templates can be exported to
    various external formats (HTML, LaTeX, PDF, ODT etc.) with pandoc as the
    converter backend.
	"""
	
	homepage = "https://rapporter.github.io/rapport/"
	cran = "rapport" 

	version("1.1", md5="290e1191de26d48ca0487c8d8bf152d7")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rapportools", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
