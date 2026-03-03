# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLattices(PythonPackage):
	"""Lattices is a package for the construction of lattices from a set of nodes and"""
	
	homepage = "https://github.com/dit/lattices"
	pypi = "lattices/lattices-0.3.5-py2.py3-none-any.whl" 

	version("0.1", sha256="43e424ecf6f527afe4512a5b93fe4b630b6b773c9113efadf67aaccabbd64d0b", expand=False, url="https://files.pythonhosted.org/packages/b5/48/78cfcb716886b3c54ff6b09979216c6e4242bca5857176d8163e4f883518/lattices-0.1-py2.py3-none-any.whl")
	version("0.2.0", sha256="4cefba4c921cde742a7a8ec5a9151aa0ddd4214ad48d4d5a90c3a24178da8072", expand=False, url="https://files.pythonhosted.org/packages/de/99/5c805e738cfbb60194215835285497558820fa791f6ac7a95e961ac174b8/lattices-0.2.0-py2.py3-none-any.whl")
	version("0.3.0", sha256="8757aae6673ae3843a5d006793b4ead18cebd8115306ebbc936f5cc936775952", expand=False, url="https://files.pythonhosted.org/packages/46/99/88b10f0d5c54d0a3e46013b498b36c5acb696a7bfcf6002bff0262178d9b/lattices-0.3.0-py2.py3-none-any.whl")
	version("0.3.1", sha256="c3dea5c29f9393d42fc679753ac9c0652cac88db4f230d590b167deea2e76641", expand=False, url="https://files.pythonhosted.org/packages/4d/40/7be4d30618b92b4d5e228f87ec2e349f446945c40e7a56ba9fe7daa2fe0b/lattices-0.3.1-py2.py3-none-any.whl")
	version("0.3.2", sha256="3b5441e11ec4835b1dfe35d53af8711afe6b546b025f6f50bbb436ae40a83eb2", expand=False, url="https://files.pythonhosted.org/packages/c3/0c/6fefcdc4b16838de1b7ff82f04c53a4d015bbc61dd3b1ce5ff21add89302/lattices-0.3.2-py2.py3-none-any.whl")
	version("0.3.3", sha256="77e44b5121ffd12dd321b04283ee267cc47482907b7b003f984f49c22814640a", expand=False, url="https://files.pythonhosted.org/packages/1f/ce/33cc891738267b684ebae3f6ceb6cb4a8ae939342f7278bd87f03d00e364/lattices-0.3.3-py2.py3-none-any.whl")
	version("0.3.4", sha256="ba2b7fe706528fb8a4a29ee5368dab0d4c1ace48373e19945a6ec2e6cb853fdc", expand=False, url="https://files.pythonhosted.org/packages/46/a1/4a2d476bed710f5208201366fe421b79eecbde53d3628b958ec00e8d5b39/lattices-0.3.4-py2.py3-none-any.whl")
	version("0.3.5", sha256="600b5f5bf45980822952f565a821748182ca303ff96a2e4eaf787cbd21632808", expand=False, url="https://files.pythonhosted.org/packages/59/60/3a3d5e8667551328c9df7899cd952c4d50ca1e1a6ef94763cac4bc71ffb3/lattices-0.3.5-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3:", type=("build", "run"))
	depends_on("py-networkx", type=("build", "run"))

# {'networkx': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'codecov;extra=="dev"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'hypothesis;extra=="dev"': ['0.3.0', '0.3.1'], 'ipython[nbconvert];extra=="dev"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'pytest;extra=="dev"': ['0.3.0', '0.3.1'], 'pytest-cov;extra=="dev"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'sphinx;extra=="dev"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'ipython[nbconvert];extra=="doc"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'sphinx;extra=="doc"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'nxpd;extra=="plotting"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'codecov;extra=="test"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'hypothesis;extra=="test"': ['0.3.0', '0.3.1'], 'pytest>=2.7.3;extra=="test"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3'], 'pytest-cov;extra=="test"': ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'nxpd;extra=="dev"': ['0.3.2', '0.3.3', '0.3.4', '0.3.5'], 'pytest>=2.7.3;extra=="dev"': ['0.3.2', '0.3.3'], 'pytest>=4.4.0;extra=="dev"': ['0.3.4', '0.3.5'], 'pytest-xdist;extra=="dev"': ['0.3.4', '0.3.5'], 'pytest>=4.4.0;extra=="test"': ['0.3.4', '0.3.5'], 'coverage[toml];extra=="dev"': ['0.3.5'], 'flake8;extra=="dev"': ['0.3.5'], 'flake8-awesome;extra=="dev"': ['0.3.5'], 'flake8-bandit;extra=="dev"': ['0.3.5'], 'flake8-broken-line;extra=="dev"': ['0.3.5'], 'flake8-bugbear;extra=="dev"': ['0.3.5'], 'flake8-coding;extra=="dev"': ['0.3.5'], 'flake8-commas;extra=="dev"': ['0.3.5'], 'flake8-docstrings;extra=="dev"': ['0.3.5'], 'flake8-import-order;extra=="dev"': ['0.3.5'], 'flake8-rst;extra=="dev"': ['0.3.5'], 'flake8-rst-docstrings;extra=="dev"': ['0.3.5'], 'flake8-self;extra=="dev"': ['0.3.5'], 'flake8-todos;extra=="dev"': ['0.3.5'], 'radon;extra=="dev"': ['0.3.5']}