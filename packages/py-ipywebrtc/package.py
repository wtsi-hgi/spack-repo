# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIpywebrtc(PythonPackage):
	"""WebRTC for Jupyter notebook/lab"""
	
	homepage = "https://github.com/maartenbreddels/ipywebrtc"
	pypi = "ipywebrtc/ipywebrtc-0.6.0-py2.py3-none-any.whl" 

	version("0.1.0", sha256="4408da9326a101397ed6e882ec16511d8093b2daf04c7fbd2670267506e52416")
	version("0.1.1", sha256="2130df21864d75f07e0f4de2d98696ad669023b62554f828ce6f90fc3fb3e139")
	version("0.1.2", sha256="aa49b2aee1b1abd3ab1d7d031b7b3001c70d21b8d88f53164228a36d09a8515f")
	version("0.1.3", sha256="e2416e409c4fc377fa115c52524606c7aafe7362309960f68266c5ef52309ec5")
	version("0.2.0", sha256="3914fbcafb81e74decbe9f8b3a466f30865d23d14a5a0f4836a3cb91d139ee47")
	version("0.2.1", sha256="5541d0b4bf6cbaddce9e0add46b5839df1b6a5de3828ebcead85c10b9b20d954")
	version("0.3.0", sha256="ae6b7aeb93a82852821a74cfbc88d0b340fd137ce245ae1c18641a25a7edb826")
	version("0.4.0", sha256="4812578f74252607c8e3fbd272fd86875461a37f861f15f44061b3446dab7bc4")
	version("0.4.1", sha256="cd84a45bed211ef04c0a2b2977d7809cd8b782ef4cac6d7b9e49dd27eac7a483", expand=False, url="https://files.pythonhosted.org/packages/b5/8f/7fcea04290388263a5e85b7087ef23ae0d80b4676c1ce372d99fd3c893d0/ipywebrtc-0.4.1-py2.py3-none-any.whl")
	version("0.4.2", sha256="c3cd1e863d91168680fabb76980d9b81a75e6970aa89dab3130dbc25dc13e377")
	version("0.4.3", sha256="77896cc873d7641b0fda4b90f665f8ec8fd4c25fd6a39bf68f8d530a21645ba9")
	version("0.5.0", sha256="89fb07b296916c3d231c802419e2951fc6825fa81d87bab325d7edf86721083f", expand=False, url="https://files.pythonhosted.org/packages/65/6b/b78b2b6f96fb2299eebae3083d3625cedb62a35ddc9815897f25c8093edd/ipywebrtc-0.5.0-py2.py3-none-any.whl")
	version("0.6.0", sha256="01a6c9d79ab937c280ce4635a149c7b681457e99ea779c00c7a6aa44ee6916f8", expand=False, url="https://files.pythonhosted.org/packages/e9/11/4b83894a009ef522b5751881e21ffec55d56b0900c0b788e2906ec01c51d/ipywebrtc-0.6.0-py2.py3-none-any.whl")
