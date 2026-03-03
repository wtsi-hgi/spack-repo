# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyConfigs(PythonPackage):
	"""Configuration for humans"""
	
	homepage = "https://bitbucket.org/moigagoo/configs"
	pypi = "configs/configs-3.0.3-py3-none-any.whl" 

	version("0.1", sha256="d29ed14bb0bb9cd03909fc96375df9e1d4ddef6c1a451a091264578ee37d0f3a")
	version("0.2", sha256="37ff7937001e27cdf27177f351673a45c878cb4d10083fda97d671c799b46432")
	version("0.3", sha256="1803e67dd2f836220a02164c23aceb2c67c8d60128699d75d046c409a336301d")
	version("0.4", sha256="29a6d19f0703678f783ad3bca654556b71077f02506612450d74c1f66062339d")
	version("0.5", sha256="9a2835fe479a5577826b60268e9809203edb53a6580479ecbac283565dc217ec")
	version("0.6", sha256="d2ce30dc158bbb113f1dbef94747c836ea0020f1ed9a27fc3ec64c35264969ad")
	version("0.7", sha256="a3ee69f791ecd67308d0f9a368a7ab7ba36ddb4aa9c2e4f896b09fa2679ac931")
	version("0.8", sha256="f3edc64fdb22c81e88ecc66271a6ca01d21f0072a63762664f0f4cff69308b8e")
	version("0.9", sha256="45bd6a1c793c91202a863ba8f3ffc1d36bbc7821c146d6a9c2c22258a731a681")
	version("1.0", sha256="13c9e8c46975086e976ccfbdfd8c3e8fb250a8031b622fd3efbd110eadac328d")
	version("1.1", sha256="8837fea9d512d40a34c6bd6c168364624dc995baee2989c57a0872eeb5ee5bf9")
	version("1.2", sha256="a4ab8cbde77a5e178066529adf90cb9bec393d1419bcb278ac30fdd58aaacaec")
	version("1.3", sha256="36edc411ac892887177156d2776b3c2c60e2e573ba2f6015c9286511fb0d88b4")
	version("1.4", sha256="2f5c8ac23abdf977032330107fc159053d20058f1d885c4e128b4ddbbd69cce5")
	version("1.5", sha256="d2d72c3ce702d6b6758d904d0c022f769c2611c79f6c6dc0b550592955b7e221")
	version("1.6", sha256="8af84120a98b4fd238f124fbc9396495bfa877481a685c337dfcc32ef98e34ce")
	version("1.7", sha256="2237b2cbdacbb3dda20433a5ee47f81d2dcc874c9b1772ef6a205e8e21018adf")
	version("1.8", sha256="63682dfb97d5c655c1e32983230f6e12d3b40f7fb391195a228a58c615768fe0")
	version("1.8.1", sha256="6bb59a888648e8db76e40aa834cae68a00f66eb2457cc95100c353b81af561f8")
	version("1.8.2", sha256="6e2b6a69f1373953b2a3a0d33a3a8d100ec469ac5999fcb7014cfc44979d3758")
	version("1.9.5", sha256="c53d0003c20bc315802fc70c3dac7245cb0d0e8172e19bb872307d0443a8e6fc")
	version("2.0.1", sha256="64734aad9459cb0ba16cd95c8c7686f8850b59d0fb04e5bd7d441a5c801369ca")
	version("2.0.2", sha256="53a94c4549dc1028c2ab92406d3c2c94a203387e54c265a25a7d991d171a4364")
	version("2.0.3", sha256="8df92814e378998792a775dfb68b8fca69fce888090994ba7be8ccc4ae0c969f")
	version("2.0.4", sha256="9897bdb63380809429736b795c2a1ac9d11294fe32c8f9d044816e2c079b508e")
	version("2.0.5", sha256="bcbfb128c52e83f0b7713a50affff1b0797211ac03e53cd0ed75f4b1e6df01cc")
	version("2.0.6", sha256="fb8e18a85cd18576bb02be7fc2cd2e3e8e68cced72ff8f79c0a304212c904a31")
	version("2.0.7", sha256="49331d9d7c4ae4ff4b80749b848b5e96db8ea6b61dd9388dc76d9ab99366a6f2")
	version("2.0.8", sha256="5410895eec2b2ec07b099a6dd2d9f6a11216774f1691f84a35e735644b6933d4", expand=False, url="https://files.pythonhosted.org/packages/86/fa/4a10e1f1c183c4b1375ab1c4781b02d51e566cab3b4342976e4df54feeaa/configs-2.0.8-py33-none-any.whl")
	version("2.0.9", sha256="73f7b874f9ced0f5b24ec7888256c03c300a5f346e879083c1d508c9a829014d", expand=False, url="https://files.pythonhosted.org/packages/77/2f/17ae3ba09a476c4fed0fc86cad8a9f01b96dbcee38667c0fdb015940c16b/configs-2.0.9-py3-none-any.whl")
	version("3.0.1", sha256="914c60963a695a6f356d8b9c66bd6e551bd95b623e4de86ba787bad231c8471e", expand=False, url="https://files.pythonhosted.org/packages/89/85/36e230cfaa504c99ca20773b491171cfc568bf9971b11f220d5d208f0d97/configs-3.0.1-py3-none-any.whl")
	version("3.0.2", sha256="4310eb87d4d09697e46c20fa7f22d047e6f4f6db83ed2e746c1508e828921451", expand=False, url="https://files.pythonhosted.org/packages/1f/33/ec91d1d0f8d3c8e8e8d52a84db313eb2ee31926701a225c08c8739bfa543/configs-3.0.2-py3-none-any.whl")
	version("3.0.3", sha256="3aa54e99b012ece70d30b7926d9e8fa159544ca27445ec2776254e25ccc190a7", expand=False, url="https://files.pythonhosted.org/packages/b0/ac/20230cd79c583ccf1e81f328befdffc1f8a23aee814c3261220954099c2a/configs-3.0.3-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
