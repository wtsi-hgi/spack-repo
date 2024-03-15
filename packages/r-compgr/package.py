# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompgr(RPackage):
	"""Complete Annual Growth Rate Generator

	It is designed to streamline the process of calculating complete annual growth rates with user-friendly functions and robust algorithms. It enables researchers and analysts to effortlessly generate precise growth rate estimates for their data. For method details see, Sharma, M.K.(2013) <https://www.indianjournals.com/ijor.aspx?target=ijor:jfl&volume=26&issue=1and2&article=018>. It offers a comprehensive suite of functions and customisable parameters. Equipped to handle varying complexities in data structures. It empowers users to uncover insightful growth dynamics and make informed decisions.
	"""
	
	cran = "CompGR" 

	version("0.1.3", md5="778cb9dc78ee13d02003b4a40842011e")

	depends_on("r@2.10:", type=("build", "run"))
