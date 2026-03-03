# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPycddlib(PythonPackage):
	"""A Python wrapper for cddlib"""
	
	homepage = "https://github.com/mcmtroffaes/pycddlib"
	pypi = "pycddlib/pycddlib-3.0.2.tar.gz" 

	version("1.0.2", sha256="26d07c058ba8ea948d26234c351c378efd21b368ab6b36d06a3945a097be112d")
	version("1.0.3", sha256="b53e22687e1a5e03d4660022ff9813f3417e63268e4d60caba985d805b9dca39")
	version("1.0.4", sha256="d42e50e21310826121163a3c73b40ed0e52e3b29f9cf97fd3a26a7cd71f6664f")
	version("1.0.5", sha256="9ad8dc8b4c130744ec9c020857c12d11a97a081bd4db8c5d656f49979aa6697b")
	version("1.0.6", sha256="4646164928f755af8d22e42ab63fc038f14da6672116a58f6d6efc86c65ab214")
	version("2.0.0", sha256="621e4a1d9bf187093918c455309937024c47f43253122dea3276bbb958fdf170")
	version("2.1.0", sha256="a5c9dea56b1e1ba65963e4145db9fd638c7ddf6b8d4b81882d3caaa648832615")
	version("2.1.1", sha256="38e49234824c95391e8f55ae34c6da15886d34f221f05316e67c9ea6a54624e1")
	version("2.1.2", sha256="b073b7b1a88c56c5de8ef9ff8e9f7b11123f1a0657243d12ffba57f0958ccf2f")
	version("2.1.3", sha256="185d07651bfa72f8c48b894d1137f01b87f6c462d6f4dc620e5d7938251794b0")
	version("2.1.4", sha256="5145e8be222aeb9ee34c0d5f3df36362add3499999134719adbd5d27fb393900")
	version("2.1.6", sha256="c7c87c0992edb608e999c84b3977bdc36035e651bed4ef089427f3b0e840aa3d")
	version("2.1.7", sha256="6d0be26049ee303181a1433fc5d57c78fe231b458bdf86855887ca8de83fb55e")
	version("2.1.8.post1", sha256="7c9a486b328236e518d253cbcfdbe912aa27f37e141b20cd526ac14471933064")
	version("3.0.0", sha256="799aa64c6f2e3d88d65f420931322a03a080d956a7d9c540b0aa56e9ba5b6b55")
	version("3.0.0a5", sha256="35c195a3a3249428bd76d82fc2f8b1e747f472608605fae88ce147298a738c71")
	version("3.0.0b1", sha256="800aefea12bcb406c69cef3aaa9cc102ac2abd1603fe17b46533ddbebf47186c")
	version("3.0.0b2", sha256="2ac263104cbea411c6c162167849f4d4632933749ac11a2d1c980959840898d1")
	version("3.0.0b3", sha256="5b7ad8e44347ef880dd5a5ccfaf8e6d177f0f7b1d7c9db68c0cebabaa4b0ead3")
	version("3.0.0b4", sha256="d95a963c628f3a58ddb2dfa5a05bb2cca9fef32d8a23ff368d265fac7e7ab787")
	version("3.0.0b5", sha256="f482008f4cf9be5de127c817cb96e7c79460cec7bda858b5a342cf8888877c5b")
	version("3.0.0b6", sha256="cc44a412deed6fe96e4c28cdec53f85498abcb955c44cf5a8beb5fcb0553d95d")
	version("3.0.1", sha256="ff9fe83fa58e5c6b107683f16ddf1068d6ca23b4a0e423b4413a67a0b76e531b")
	version("3.0.2", sha256="50f43f039818ab97c8cb44345eed9a365dae66789ce11cc8c95a74134a8907a7")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-cython@3:", type=("build"))
	depends_on("cddlib", type=("build", "link"))
	depends_on("gmp", type=("build", "link"))
	depends_on("python@3.9:", type=("build", "run"))
