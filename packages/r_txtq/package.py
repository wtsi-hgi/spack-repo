# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTxtq(RPackage):
	"""A Small Message Queue for Parallel Processes

	This queue is a data structure that lets
  parallel processes send and receive messages,
  and it can help coordinate the work
  of complicated parallel tasks.
  Processes can push new messages to the queue,
  pop old messages, and obtain a
  log of all the messages ever pushed. File locking
  preserves the integrity of the data even when
  multiple processes access the queue simultaneously.
	"""
	
	homepage = "https://github.com/wlandau/txtq"
	cran = "txtq" 

	version("0.2.4", md5="dd5e8b88fd514970c9ec3bc007abb418")

	depends_on("r-base64url", type=("build", "run"))
	depends_on("r-filelock@1.0.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
