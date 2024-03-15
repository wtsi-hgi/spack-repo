# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcessx(RPackage):
	"""Execute and Control System Processes.

	Tools to run system processes in the background. It can check if a
	background process is running; wait on a background process to finish; get
	the exit status of finished processes; kill background processes. It can
	read the standard output and error of the processes, using non-blocking
	connections. 'processx' can poll a process for standard output or error,
	with a timeout. It can also poll several processes at once."""

	cran = "processx"

	license("MIT")

	version("3.8.3", md5="ad4eef6b9a21f570f8686c0157712ddf")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ps@1.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
