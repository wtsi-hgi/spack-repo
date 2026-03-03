# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuckrock(RPackage):
	"""Data on Freedom of Information Act Requests

	A data package containing public domain information on requests made by the
             'MuckRock' (https://www.muckrock.com/) project under the United States
             Freedom of Information Act.
	"""
	
	homepage = "https://github.com/Ironholds/muckrock/"
	cran = "muckrock" 

	version("0.1.0", md5="142412337d78191c8ead682e78839885")

	depends_on("r@2.10:", type=("build", "run"))
