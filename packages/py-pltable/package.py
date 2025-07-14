# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPltable(PythonPackage):
	"""Python 3 library for easily displaying tabular data in a visually appealing text table format"""
	
	homepage = "https://github.com/platomav/PLTable"
	pypi = "pltable/PLTable-1.1.0.tar.gz" 

	version("1.0.0", sha256="756f6f5a86b3eff73b21fb9e2bccdc878d90135aabb5eb4e85ce16dd5e1d2d7a")
	version("1.0.1", sha256="e6ddc74adde31501af421f29d52120cbab8ee6bd710cf8940a395d3433663fa7")
	version("1.0.2", sha256="1a34a9999ad74dcd3ba73dd602ff5853f699030d7a2e4a0469e9dacaf763bafc")
	version("1.1.0", sha256="dc8eb7cb9721a7090dc7a5976fbec7d3ef6b82a61f86c3b98700571a3f10401a")

	depends_on("py-setuptools", type=("build"))
