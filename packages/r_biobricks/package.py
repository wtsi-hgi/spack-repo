# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiobricks(RPackage):
	"""Access Data Dependencies Installed Through 'Biobricks.ai'

	Provides an integrated data management solution for assets installed via the 'Biobricks.ai' platform. Streamlines the process of loading and interacting with diverse datasets in a consistent manner. A list of bricks is available at <https://status.biobricks.ai>. Documentation for 'Biobricks.ai' is available at <https://docs.biobricks.ai>.
	"""
	
	cran = "biobricks" 

	version("0.2.2", md5="80f50523adfc2c9f0c1b3d7f6b04515f")

