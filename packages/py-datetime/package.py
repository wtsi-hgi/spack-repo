# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDatetime(PythonPackage):
	"""This package provides a DateTime data type, as known from Zope. Unless you need to communicate with Zope APIs, you're probably better off using Python's built-in datetime module."""
	
	homepage = "https://github.com/zopefoundation/DateTime"
	pypi = "DateTime/DateTime-5.5-py3-none-any.whl" 

	version("2.11.0b1", sha256="2dd683984ab566bf172a8ea6def0db166160930149b78916473e02622ee03a39")
	version("2.11.1", sha256="1b6930969e66558d0d33fc3ab96b88123c3959bd9c571f5caa56cf52a231bd55")
	version("2.11.2", sha256="aa4012027c62cce9be44310c0b0ed89276765ccb3f9ea309ef6e2e63b4a00feb")
	version("2.12.0", sha256="575043033ce88da7477c130f28ecfc19b63779cf2211b6f72bb716250ad76c69")
	version("2.12.1", sha256="1bfc8ec253fca34400c14bbbc7f4265ca01342fe66f04cd5468deb4604dcaecb")
	version("2.12.2", sha256="c95c7bf53288c2c707597a8eac31892bb41dbd3704e8576df4b1fe9c28100e3b")
	version("2.12.3", sha256="64fc253a685342b396a055658991c18d6938b44e4dcf50c842c63593485447bf")
	version("2.12.4", sha256="b2a7460ec85548f40ab8462236f624c086b3b5142af40aa3360e97bc84c3bb05")
	version("2.12.5", sha256="f7ab0fcb8ad64dc189ef3cfb7ccde3ca9a9bdee7c18c271edd42b58abea0d162")
	version("2.12.6", sha256="35ad061643d859ecfa83a66af7b0a0eb739911e597b23442f079a03937c84916")
	version("2.12.7", sha256="e57d9e0c402f1b06560357777895e0e259bd4ca6924730f70433887811eaacc3")
	version("2.12.8", sha256="f0f49bb2921a0f6e0520e14613b4bf4321fa1874558f384b388ce029a7536807")
	version("3.0", sha256="2576bc9e93b746560c09237c57c72bbd7605255662b3e015977b41a26a4a2afe")
	version("3.0.1", sha256="6cc3493d26673909db4ae0e5a27265fea09f26ea3ac2daaadff31b330e1de35b")
	version("3.0.2", sha256="0205beba610b8ec1190ffe66d808b6d9d05dfde67071841395cb033ba43ffb45")
	version("3.0.3", sha256="076155f509ac122effb2be32576540ba4a5cca56de557c4bc206980e4017a8c3")
	version("3.0a1", sha256="9a7f214afc29271f41ad613fa6b0dfc9e662d685b755071a7822025af60cf0ba")
	version("3.0a2", sha256="db55efd7f4c39a529a755a3df3d6447ee9a0b070ccf26d46aada9e1b4d4caa7c")
	version("3.0b1", sha256="5893afa3e7269bbb09c8e525e81b2cc5c800c0dfb06222334d702bfaed6c7b62")
	version("3.0b2", sha256="6da2d7b69f1639b85bae55b9ad45f8eaaccc683e0ea11d5c432bb774e79ea30f")
	version("3.0b3", sha256="e216b6d8d190726208f3e92fa9065b4a389f1a8534e0a205bc2dec2d67179b4f")
	version("4.0", sha256="cb66b32c6d2fad9f2222addaf2919ee35379f7fc001807894412e3fc72b4818d")
	version("4.0.1", sha256="a4073f0549862278aad3986982e835092009fca681f9d4a719112eb24964695b")
	version("4.1", sha256="2f387e08b99bb872825485e7a3172b40dfb3a77965cd03137c0d4ea3a4dd8b39")
	version("4.1.1", sha256="10936a83bb9051a70b0f0feb227fe147b4362c5467fe1faedf2c97d8850ad371")
	version("4.2", sha256="6a7d0650cf9cfc10b0e152fa6c667176cff7cd68b93040c10aca868d4a4617c0", expand=False, url="https://files.pythonhosted.org/packages/0d/db/511934e34360fe0cfe91fc58483b25d8a9c516264ff2877dadb11a0612cd/DateTime-4.2-py2.py3-none-any.whl")
	version("4.3", sha256="371dba07417b929a4fa685c2f7a3eaa6a62d60c02947831f97d4df9a9e70dfd0", expand=False, url="https://files.pythonhosted.org/packages/73/22/a5297f3a1f92468cc737f8ce7ba6e5f245fcfafeae810ba37bd1039ea01c/DateTime-4.3-py2.py3-none-any.whl")
	version("4.4", sha256="4fcca115ddb466a1104df08d5c2a2f5805d14ca317800e1bfcea8f3d69f66e57", expand=False, url="https://files.pythonhosted.org/packages/e7/3b/1f34298fc26ced9c699434f9d1a085f526daf2b87da7d259f874362f344a/DateTime-4.4-py2.py3-none-any.whl")
	version("4.5", sha256="ec9894c438cdd54dc31578b1b43c79b11f8111dbeb066e372548a0a78a3bec46", expand=False, url="https://files.pythonhosted.org/packages/1d/bb/8e43c08cf8520816abe7afc5b5bff2a83807f371af90e7067d348b6a29ef/DateTime-4.5-py2.py3-none-any.whl")
	version("4.6", sha256="9c7657bc624e866a0f6bf0c5e2e49d3fbf4082cc333992bb6274f7c0120b53cd", expand=False, url="https://files.pythonhosted.org/packages/02/97/4752d5fb6ed589cfea4d70866dfaede0a7296327aa16065516660c52f3b6/DateTime-4.6-py2.py3-none-any.whl")
	version("4.7", sha256="b8d2d605cfb5fed0da86f9ad64d0973c6f84b21939d49265e135811b33ee8113", expand=False, url="https://files.pythonhosted.org/packages/da/79/9a97c449d65ea6cc6eb382a73fbd39919f106083a7ab3aeff2f209083718/DateTime-4.7-py2.py3-none-any.whl")
	version("4.8", sha256="b7d173fbe15c10a53575f56d2570b6e956c0a95e4be03479517a00791b19917d", expand=False, url="https://files.pythonhosted.org/packages/da/ee/5fae5137fa4c755b78b6377e2e1e870696166682973d3d575a002b520f8b/DateTime-4.8-py2.py3-none-any.whl")
	version("4.9", sha256="ed114f161d7b8ec04b84f398de3fc3b973b2b7273f812aa109ee64358a01db64", expand=False, url="https://files.pythonhosted.org/packages/24/1a/cdac35c7627578939d509d436123328dea641c24e9f76c15a9bbe1016af7/DateTime-4.9-py2.py3-none-any.whl")
	version("5.1", sha256="97f5ec489e75e26c2e7b4e4b37dc001389814dca1f14ec046c7f9270cf3cee9e", expand=False, url="https://files.pythonhosted.org/packages/3e/9f/8d589a4635da1ec033072ec59e8283faf58181542d62261277c4c3c4afe1/DateTime-5.1-py3-none-any.whl")
	version("5.2", sha256="25250fb36f7184dad805faaf3f012e0b36f353cd97518e8f232babef5c53596e", expand=False, url="https://files.pythonhosted.org/packages/95/88/3b9d4042b396221a132180b392ab2a174031a6fb579f7927f3909fc183a7/DateTime-5.2-py3-none-any.whl")
	version("5.3", sha256="05669f035ec7ccb24443bda8572078c381edf79c813186f627e9e8e5c6e8e6e6", expand=False, url="https://files.pythonhosted.org/packages/d3/63/dced85cf2970b5d363e501a10aa051e71caea3ad10a60b7a57794f43a4b8/DateTime-5.3-py3-none-any.whl")
	version("5.4", sha256="88caf4d2441fe479038f4740a1071953686f7c1ed6c9e8c7df9ebe84e592f0c6", expand=False, url="https://files.pythonhosted.org/packages/ff/d5/f508192a563ab7415d1efbbe8d39cb9f0e510a1f6aaee3ca7d4ffed2a194/DateTime-5.4-py3-none-any.whl")
	version("5.5", sha256="0abf6c51cb4ba7cee775ca46ccc727f3afdde463be28dbbe8803631fefd4a120", expand=False, url="https://files.pythonhosted.org/packages/f3/78/8e382b8cb4346119e2e04270b6eb4a01c5ee70b47a8a0244ecdb157204f7/DateTime-5.5-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-zope-interface", type=("build", "run"))
	depends_on("py-pytz", type=("build", "run"))
