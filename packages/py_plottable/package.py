# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPlottable(PythonPackage):
	"""Beautifully customized tables with matplotlib"""
	
	homepage = "https://github.com/znstrider/plottable"
	pypi = "plottable/plottable-0.1.5-py3-none-any.whl" 

	version("0.1.0", sha256="dc25dc1629b3742ef8fac4286a394d4512c8c53f828081ef58d36ad6fe523d39", expand=False, url="https://files.pythonhosted.org/packages/af/4a/bff82c4871c40e6f436828a4731c3678ecf5fa18dc4b5e37b9137c2ad27c/plottable-0.1.0-py3-none-any.whl")
	version("0.1.1", sha256="5e1ae204005dc819cea5f1b32ebf6010469006ef018cef126f137edcd22b185a", expand=False, url="https://files.pythonhosted.org/packages/99/95/77871a2a00b39ee95bce0020fe79abd8b0bca7f96f575551b0068e38274b/plottable-0.1.1-py3-none-any.whl")
	version("0.1.2", sha256="767e7e87964190fc7acfad2412ab697a1f3153d5686a8b6ddba0e6ff08a9f7bf", expand=False, url="https://files.pythonhosted.org/packages/ae/41/16c31e0687563ef2cc1ab60b6032f1546499875f475d1bd9d5e5cc112b1e/plottable-0.1.2-py3-none-any.whl")
	version("0.1.3", sha256="5b0fa7ff3e28441d16391eee8fa69139c02f27a4feff1a2f1d292fa755bb35c8", expand=False, url="https://files.pythonhosted.org/packages/d2/eb/ed3cc6ed65470b119175090ac48e7dc11c741b2ae70a127faae5d1e25d5c/plottable-0.1.3-py3-none-any.whl")
	version("0.1.4", sha256="0e9e9bb646243640c70081746b270a311caae467aaf24fb771bf4e796a0206a8", expand=False, url="https://files.pythonhosted.org/packages/e9/f7/44a8be027dbb314713ab2d58d26bfe5d853d125db8fb32df32b4871216e2/plottable-0.1.4-py3-none-any.whl")
	version("0.1.5", sha256="5c5d1128d90065fc940e5c8445b2603d253909745bb0cee0c9828651b812441c", expand=False, url="https://files.pythonhosted.org/packages/ca/cf/23ea4b6f9460312604ed67b74e7db3e702fcaefc04743224ef1cdda663f4/plottable-0.1.5-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))

# {'Pillow(>=9.2.0,<10.0.0)': ['0.1.0', '0.1.1', '0.1.2'], 'matplotlib(>=3.6.1,<4.0.0)': ['0.1.0', '0.1.1', '0.1.2'], 'numpy(>=1.23.4,<2.0.0)': ['0.1.0', '0.1.1', '0.1.2'], 'pandas(>=1.5.1,<2.0.0)': ['0.1.0', '0.1.1', '0.1.2'], 'matplotlib\r': ['0.1.3', '0.1.4', '0.1.5'], 'numpy\r': ['0.1.3', '0.1.4', '0.1.5'], 'pandas\r': ['0.1.3', '0.1.4', '0.1.5'], 'Pillow\r': ['0.1.3', '0.1.4', '0.1.5'], "pytest;extra=='development'\r": ['0.1.3', '0.1.4', '0.1.5'], "black;extra=='development'\r": ['0.1.3', '0.1.4', '0.1.5']}