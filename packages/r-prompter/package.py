# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrompter(RPackage):
	"""Add Tooltips in 'Shiny' Apps with 'Hint.css'

	In 'Shiny' apps, it is sometimes useful to store information
    on a particular item in a tooltip. 'Prompter' allows you to easily 
    create such tooltips, using 'Hint.css'.
	"""
	
	homepage = "https://github.com/etiennebacher/prompter"
	cran = "prompter" 

	version("1.1.0", md5="8555f32db73800993bb269842a6c78e7")

	depends_on("r-shiny", type=("build", "run"))
