# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySchpl(PythonPackage):
	"""Hierarchical progressive learning pipeline for single-cell RNA-sequencing datasets"""
	
	homepage = "https://github.com/lcmmichielsen/scHPL"
	pypi = "scHPL/scHPL-1.0.5-py3-none-any.whl" 

	version("0.0.1", sha256="c222af19ac7dd016afbc33118a70121e754c77a296ef60dc777b37f7fc1f8a97", expand=False, url="https://files.pythonhosted.org/packages/19/30/a9d1a74d753a8b1e60fb9d4b3d41776c024e654c57d56a255de589c6607d/scHPL-0.0.1-py3-none-any.whl")
	version("0.0.2", sha256="bcbca67da8459116895960786bfb7b3082a12b333af3ff238c758496d06fa6b4", expand=False, url="https://files.pythonhosted.org/packages/01/1d/1f51fb03ab53c885c735324a85e8260f7ab816d8e41b041d94ecdb77d9a8/scHPL-0.0.2-py3-none-any.whl")
	version("1.0.0", sha256="beb68c8aa0bf4c1b0bf478ee110112349794ff3699379689cee9131647363fbb", expand=False, url="https://files.pythonhosted.org/packages/aa/4e/3abf1f88e584e587c2c3e980e6f608249c91a5147626fd010569ecc98c0f/scHPL-1.0.0-py3-none-any.whl")
	version("1.0.1", sha256="c0b55087317f8729a49d2e7c0c2c68e13794376dc0d8c2c416f836d8856f2fbd", expand=False, url="https://files.pythonhosted.org/packages/de/4f/addbdc1302a3107d10633f52160d4537bca8c3726b7c2037af55289501d3/scHPL-1.0.1-py3-none-any.whl")
	version("1.0.2", sha256="9ca277c82d9b4ef11318fcf43a79ccd2ebd909ab56e29095b5cc99585bb3c4e2", expand=False, url="https://files.pythonhosted.org/packages/f3/2d/c9df8195d8ee96aa7156d960837a8d081e8eee95d09ae1b10025177458b7/scHPL-1.0.2-py3-none-any.whl")
	version("1.0.3", sha256="8ac34606653c2aabe58932cab5e7c2296b26912c5f5da2f2db66c3e08b6a8d68", expand=False, url="https://files.pythonhosted.org/packages/ff/de/0f55c215dc6348d2f86f786499592d4ea50bf6a4fd580e43abe9a921e814/scHPL-1.0.3-py3-none-any.whl")
	version("1.0.4", sha256="1d831411ab72e2e26fac46644d8b0e7245a4e43b1e7744258e8ee52e67263943", expand=False, url="https://files.pythonhosted.org/packages/71/fe/9d8b999436e7192b2303650d9e8f592124f51144479173e41673f99bb1ec/scHPL-1.0.4-py3-none-any.whl")
	version("1.0.5", sha256="1d1ba8464b1853d1d72bc0ad278e51a670a028adb3d71264da2e186045bce225", expand=False, url="https://files.pythonhosted.org/packages/dc/c0/ffa98fba041fa01e7863d424422b20cceade8ef9eec68c7058848cdb0ecd/scHPL-1.0.5-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.6:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-newick", type=("build", "run"))
	depends_on("py-anndata", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-seaborn", type=("build", "run"))

# {'numpy(~=1.19.2)': ['0.0.1', '0.0.2'], 'scipy(~=1.5.2)': ['0.0.1', '0.0.2'], 'scikit-learn(~=0.23.2)': ['0.0.1', '0.0.2'], 'pandas(~=1.1.2)': ['0.0.1', '0.0.2'], 'newick(~=1.0.0)': ['0.0.1', '0.0.2', '1.0.0', '1.0.1', '1.0.2', '1.0.3'], 'numpy(>=1.19.2)': ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], 'scipy(>=1.5.2)': ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], 'scikit-learn(>=0.23.2)': ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], 'pandas(>=1.1.2)': ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], 'anndata(>=0.7.4)': ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], 'matplotlib(>=3.3.1)': ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], 'seaborn(>=0.11.1)': ['1.0.0', '1.0.1', '1.0.2', '1.0.3'], 'numpy>=1.19.2': ['1.0.4', '1.0.5'], 'scipy>=1.5.2': ['1.0.4', '1.0.5'], 'scikit-learn>=0.23.2': ['1.0.4', '1.0.5'], 'pandas<2.0.0,>=1.1.2': ['1.0.4'], 'newick~=1.0.0': ['1.0.4', '1.0.5'], 'anndata>=0.7.4': ['1.0.4', '1.0.5'], 'matplotlib>=3.3.1': ['1.0.4', '1.0.5'], 'seaborn>=0.11.1': ['1.0.4', '1.0.5'], 'pandas<2,>=1.1.2': ['1.0.5']}