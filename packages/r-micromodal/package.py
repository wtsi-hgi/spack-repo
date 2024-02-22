# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicromodal(RPackage):
	"""Create Simple and Elegant Modal Dialogs in 'shiny'

	Enables you to create accessible modal dialogs, with confidence and with minimal configuration.
	"""
	
	homepage = "https://github.com/kennedymwavu/micromodal"
	cran = "micromodal" 

	version("1.0.0", md5="3f9a7483b5044b46b0382ba1d83d413e")

	depends_on("r-htmltools@0.5.5:", type=("build", "run"))
