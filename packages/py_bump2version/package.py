# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBump2version(PythonPackage):
	"""Version-bump your software with a single command!"""
	
	homepage = "https://github.com/c4urself/bump2version"
	pypi = "bump2version/bump2version-1.0.1-py2.py3-none-any.whl" 

	version("0.5.10", sha256="185abfd0d8321ec5059424d8b670aa82f7385948ff7ddd986981b4ed04dc819a", expand=False, url="https://files.pythonhosted.org/packages/a0/fd/cf89ed7ba5c336ab050746680167b3a49264e8c7b1a91d9b0a6dabb26b13/bump2version-0.5.10-py2.py3-none-any.whl")
	version("0.5.11", sha256="bfcc051498dda9fd9ac8634689f4516e1c20fdeeace3278932cc6e1248418b36", expand=False, url="https://files.pythonhosted.org/packages/e3/f5/2badfac824763a4fbf3b696321f8c66635b1ceb339ff3a400cc9000add0c/bump2version-0.5.11-py2.py3-none-any.whl")
	version("0.5.4-py2.7", sha256="617643594e4e26aaf9127e5ed922666808a02bcc8bf2853c4ef271526fe8217e", expand=False, url="https://files.pythonhosted.org/packages/b2/1a/8d86cb73947591ff4a9022da58a9da70d0e777068e8b9ebe5b7df5e7c50a/bump2version-0.5.4-py2.py3-none-any.whl")
	version("0.5.5-py2.7", sha256="eb0ae814e0d72fd0aca8b33d6964c1713e51f4b2185b25907366e3afd53017dc", expand=False, url="https://files.pythonhosted.org/packages/da/4c/fc46d78feeb834739fcb15c81d0a3be3b486f0eadb305eaad2b7a960d8ae/bump2version-0.5.5-py2.py3-none-any.whl")
	version("0.5.6-py2.7", sha256="77b404dd620cb1c5abbd4a0233443b95023f499cd5295e1caf6afb1efa95697d", expand=False, url="https://files.pythonhosted.org/packages/f0/80/7e0d4fbe22dbfd6e7a0472a7e0b59f2c497eee268138dae81339ee2f30ee/bump2version-0.5.6-py2.py3-none-any.whl")
	version("0.5.7-py2.7", sha256="b98f0795e17d23d60500ee7b5fbf375eee337709fbf42edcfec695e888e4f879", expand=False, url="https://files.pythonhosted.org/packages/af/0d/c87ebff85fbacdaa498bb01747cdf543ef22976def7fa1e981d51ed505e6/bump2version-0.5.7-py2.py3-none-any.whl")
	version("0.5.8-py3.6", sha256="6df32d297f7a624d4a66f06c5dfcf29ec5fafdc53cf8d0c0ee973563a8f1794d", expand=False, url="https://files.pythonhosted.org/packages/16/a5/5d8e4fc4e2217cb422d4ad63c92921bc8679fae01b5c4a09d51dd5841f13/bump2version-0.5.8-py2.py3-none-any.whl")
	version("1.0.0", sha256="477f0e18a0d58e50bb3dbc9af7fcda464fd0ebfc7a6151d8888602d7153171a0", expand=False, url="https://files.pythonhosted.org/packages/61/10/560509d9bfe8300e03d268dadec74fac7ae04a430f62e2d06d11d9e4e704/bump2version-1.0.0-py2.py3-none-any.whl")
	version("1.0.1", sha256="37f927ea17cde7ae2d7baf832f8e80ce3777624554a653006c9144f8017fe410", expand=False, url="https://files.pythonhosted.org/packages/1d/e3/fa60c47d7c344533142eb3af0b73234ef8ea3fb2da742ab976b947e717df/bump2version-1.0.1-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.5:", type=("build", "run"))
	depends_on("python@2.7", when="@0.5.4-py2.7", type=("build", "run"))
	depends_on("python@2.7", when="@0.5.5-py2.7", type=("build", "run"))
	depends_on("python@2.7", when="@0.5.6-py2.7", type=("build", "run"))
	depends_on("python@2.7", when="@0.5.7-py2.7", type=("build", "run"))
	depends_on("python@3.6", when="@0.5.8-py3.6", type=("build", "run"))
