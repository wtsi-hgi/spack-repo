# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDocrep(PythonPackage):
	"""Python package for docstring repetition"""
	
	homepage = "https://github.com/Chilipp/docrep"
	pypi = "docrep/docrep-0.3.2.tar.gz" 

	version("0.0.0.dev1", sha256="7ad9d576e4fdd9b2a68d7372644325dfacaa7b21ba273e66a9c1cb45fe6263b2")
	version("0.1.0", sha256="360ac0ea2e8b009e02dcf033d6058f28d807afcd1c3b9136b2a80acf5c9d8755")
	version("0.1.1", sha256="ede2317a6caa63b04197b69b0b511237236d9c27c962d0dfcd6ff7290b165d45")
	version("0.1.2", sha256="bd88bd864c04c5db84e65648f53816a5bc695632d5d87a389be8bafcfa1cf407")
	version("0.2.0", sha256="2533fe0c71e1f6049a22e82f7b7471f94baf05a0aed3793a73b04ab8db76c9dc")
	version("0.2.1", sha256="ef121cb4e380c7c09d7df6db20eae4987a80dd3608968a1015953ee1ff0b4074")
	version("0.2.1.post1", sha256="e6f7bbe3726e119a6aa4eeeb037d763b3b1b3a7af39fc9cb0a4645875e55c3da")
	version("0.2.2", sha256="74509f68e74d0977c787e255136df5f4c6b93a651943f464c670b46687fda425")
	version("0.2.3", sha256="7d195b6dfcf4efe5cb65402b6c6f6d7e6db77ce255887fae32c9a8288a022659")
	version("0.2.4", sha256="ec7598fc2497a50f2c6882803d78e3c3cc4f1a554645d2c43c58d53653a1be01")
	version("0.2.5", sha256="a67c34d3a44892d3e2a0af0ac55c02b949a37ced9d55c0d7ade76362ba6692d7")
	version("0.2.6", sha256="a66d07e2d4a6a0b71913b2d1a265d2f186ba624ac9043ac663c195f15f949ec0")
	version("0.2.7", sha256="c48939ae14d79172839a5bbaf5a570add47f6cc44d2c18f6b1fac8f1c38dec4d")
	version("0.3.0", sha256="8e7d87c284df6ed7c8d27e4efb40275dc61bd33d49f19c693092944019f1b922")
	version("0.3.1", sha256="ef6e7433716c0d2c59889aae8bff800b48e82d7e759dfd934b93100dc7bccaa1")
	version("0.3.2", sha256="ed8a17e201abd829ef8da78a0b6f4d51fb99a4cbd0554adbed3309297f964314")

	depends_on("py-setuptools", type="build")
