# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLogomaker(PythonPackage):
	"""Package for making Sequence Logos"""
	
	homepage = "http://logomaker.readthedocs.io"
	pypi = "logomaker/logomaker-0.8-py2.py3-none-any.whl" 

	version("0.1", sha256="831e85802c9c61def6409b0700151d7deb095e34435d4147c6522f3cff68ddbd", expand=False, url="https://files.pythonhosted.org/packages/13/28/aeef0e038e1385274315d5d435685affe9e1e571908eed5145309ada444e/logomaker-0.1-py2.py3-none-any.whl")
	version("0.2", sha256="67b16d3af46422ab09163041df3fe5f6c0002d5cfbd94c0f57b5edb7ff234f68", expand=False, url="https://files.pythonhosted.org/packages/8d/4e/9c5f02e3f353bc151c62e9d1df1fb5f843c17c06847b1607ca1fb4e434f9/logomaker-0.2-py2.py3-none-any.whl")
	version("0.3", sha256="606ce495f2467243377f08ccf4c4e1388e08a3ecd033297090a44ad34c01fbcf", expand=False, url="https://files.pythonhosted.org/packages/0c/e2/beba4555f8e4f05bc0d0215a28ce2e82f9e86747b1a27071f71fddaf6d38/logomaker-0.3-py2.py3-none-any.whl")
	version("0.5", sha256="1610e57645395d956af874753d5f7771ddb548f874c40c920df21dc885993774", expand=False, url="https://files.pythonhosted.org/packages/c1/fc/310fc2fb753b2abc13aade3d8bf76c1d3fdc8b9d77eed2555e35d1c84a1a/logomaker-0.5-py2.py3-none-any.whl")
	version("0.6", sha256="a8b6417429ec01c961dad983e8353189e3a7a29d4ee09eb63a9687d39017db26", expand=False, url="https://files.pythonhosted.org/packages/32/af/aa77e32ed7b603e0f5f6341be60fa49bb9d17d19d665ee74fa936070e5d0/logomaker-0.6-py2.py3-none-any.whl")
	version("0.7", sha256="4a34c2e2ba0898a9412662cd484b5c84559dee66ffb7dfdb3a2807abea8a5738", expand=False, url="https://files.pythonhosted.org/packages/a2/17/85d9d0c59d926f31c35cb3570d2d238086ac5eb7b3e64ccb9db7da2e9af4/logomaker-0.7-py2.py3-none-any.whl")
	version("0.8", sha256="6766a0d83de4990ea859366a661ba72c580a7b73ac3c8b526204a0be7d65a50d", expand=False, url="https://files.pythonhosted.org/packages/87/6d/9a9976674e77de3eab157e8c50667a7091058fa355fd7665eb1ab4b93c5a/logomaker-0.8-py2.py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))

# {'numpy': ['0.1', '0.2', '0.3', '0.5', '0.6', '0.7', '0.8'], 'backports.functools-lru-cache(==1.4)': ['0.1', '0.2', '0.3', '0.5'], 'biopython(==1.70)': ['0.1', '0.2', '0.3', '0.5'], 'click(==6.7)': ['0.1', '0.2', '0.3', '0.5'], 'cycler(==0.10.0)': ['0.1', '0.2', '0.3', '0.5'], 'Flask(==0.12.2)': ['0.1', '0.2', '0.3', '0.5'], 'gunicorn': ['0.1', '0.2', '0.3', '0.5'], 'functools32(==3.2.3.post2)': ['0.1', '0.2', '0.3', '0.5'], 'itsdangerous(==0.24)': ['0.1', '0.2', '0.3', '0.5'], 'Jinja2(==2.9.6)': ['0.1', '0.2', '0.3', '0.5'], 'MarkupSafe(==1.0)': ['0.1', '0.2', '0.3', '0.5'], 'matplotlib(==2.0.2)': ['0.1', '0.2', '0.3', '0.5'], 'numpy(==1.13.3)': ['0.1', '0.2', '0.3', '0.5'], 'pandas(==0.21.0)': ['0.1', '0.2', '0.3', '0.5'], 'pyparsing(==2.2.0)': ['0.1', '0.2', '0.3', '0.5'], 'python-dateutil(==2.6.1)': ['0.1', '0.2', '0.3', '0.5'], 'pytz(==2017.3)': ['0.1', '0.2', '0.3', '0.5'], 'six(==1.11.0)': ['0.1', '0.2', '0.3', '0.5'], 'subprocess32(==3.2.7)': ['0.1', '0.2', '0.3', '0.5'], 'Werkzeug(==0.12.2)': ['0.1', '0.2', '0.3', '0.5'], 'matplotlib': ['0.6', '0.7', '0.8'], 'pandas': ['0.6', '0.7', '0.8'], 'glob2': ['0.7'], 'glob3': ['0.7']}