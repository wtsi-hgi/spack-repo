# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapparmor(RPackage):
	"""Bindings to AppArmor and Security Related Linux Tools

	Bindings to kernel methods for enforcing security restrictions. 
    AppArmor can apply mandatory access control (MAC) policies on a given task 
    (process) via security profiles with detailed ACL definitions. In addition
    this package implements bindings for setting process resource limits (rlimit),
    uid, gid, affinity and priority. The high level R function 'eval.secure' 
    builds on these methods to perform dynamic sandboxing: it evaluates a single
    R expression within a temporary fork which acts as a sandbox by enforcing 
    fine grained restrictions without affecting the main R process. A portable 
    version of this function is now available in the 'unix' package.
	"""
	
	homepage = "https://www.jstatsoft.org/v55/i07/"
	cran = "RAppArmor" 

	version("3.2.4", md5="7c182e9345449ae65f6b9e80dffb0cfc")

	depends_on("r-unix@1.4:", type=("build", "run"))
