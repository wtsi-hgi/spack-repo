# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHickle(PythonPackage):
	"""Hickle - an HDF5 based version of pickle"""
	
	homepage = "http://github.com/telegraphic/hickle"
	pypi = "hickle/hickle-5.0.3-py3-none-any.whl" 

	version("1.0", sha256="50a89383ae6d6869d27b6bf49dc471a4ee548c8f37b4e65940e244f1fb9defde")
	version("1.0.2", sha256="e559353037fe627dc2929537380b258c433080773ab588e705c32e1a0fa1b262")
	version("1.0.4", sha256="4928d6251914136f77f5f76c8c7e3d5799f9909cb3fccd5907a4942edbf3b9b7")
	version("1.1.0", sha256="6a5ab37c90032dd6d81b79462819fc917072337a25614244f05de122734ac893")
	version("1.1.1", sha256="35fc10cc658ac2412a6dc00c92eccc359cd638397f850f8d963879f99e0e459e")
	version("1.2.1", sha256="a11d3ebf7f8da9c0a065b9c16c0eb760867d57c9097d7b175322179e6b8a9765")
	version("1.3.0", sha256="65044a84f775983667fc261d2af999a16143537413add9c3471af0efd7ed2470")
	version("1.3.1", sha256="904d46cc260b2dbf968261a60c16fb4f5377522732a8a7b48ca609714f3fc1ab")
	version("1.3.2", sha256="38f5cd147b7e74a3c5e6843d33f48e981d12d7140359f4773fa666dac7be9382")
	version("1.4.0", sha256="00937e3073aab1f5e54d7c9387d5a347352994efc740c2e23953f25967523ef3")
	version("2.0.0", sha256="1891d8e8b84149173b184a01f24fa05cae1b4c28d152f632f9d9f3f3ee00503e")
	version("2.0.1", sha256="4bd3d652e37af69ebaedeb2cf6db555a304d55049f4a40a9c9f0f01192cbefa4")
	version("2.0.4", sha256="038f721cd465b1b53c96e3580d2f6f5a6945680bcf5b23ef1e5d1c3d90b70146")
	version("2.0.5", sha256="efbe6f2ee7e7df39133aeece12fd1630998d1f8c7c893aebe7451e829aa90f14")
	version("2.1.0", sha256="2ee006ecb9e5107009f07d6d10b95458d48a9089c0fd7d8f67460aa4de60745a")
	version("3.2.1", sha256="25f0f3616e3878e2f693871094ab3ada44cbb0c5cc005a6dfe5572acbad094d1")
	version("3.2.2", sha256="a1cb1d79e607ef54710c9e13fd6c8aaf314b42d6d1c49d5422859c30b425b90a")
	version("3.3.0", sha256="9ae950734c716be2bad4e47546294fc42006d0fb5ae665f2dae7d37a26bb91f8")
	version("3.3.1", sha256="3e9bf1950e39ce69d9575b4d240f05d286c90fea1f505a57c57d9285a24b127f")
	version("3.3.2", sha256="cc4d689129493a59c7872806f69380d1e70d497b9911b7d7a68cd2bd18c43186")
	version("3.3.3", sha256="3771deffeeb2aee326bb16b02f066ccf718fba8dd93952293ce97ae4b98871c6")
	version("3.4.0", sha256="24ac4a142daec5761032a42ce52e5e5a9c745ca056796ca7d010ae820b4a95e6")
	version("3.4.1", sha256="60d83583269076591c06f34a275db8d908e555ef696f1b488bd3ee227fce0054")
	version("3.4.2", sha256="e51d9db88451ec2307b6cddb3267098561805a056e5759e5d65d572dafa41c46", expand=False, url="https://files.pythonhosted.org/packages/60/67/5fa83d1f6a99f4b00159b82808ce7b4373da955572be685ed4c7ef9acfab/hickle-3.4.2-py3-none-any.whl")
	version("3.4.3", sha256="34411faa56fa2b0d70bda9e37556f0cbae4f419323a86f2f97c53e54af488a19", expand=False, url="https://files.pythonhosted.org/packages/da/e5/bf2c8f13d54d8d36bcbe0e122d6a488f09f151d4af0da986eb7cd67d5f56/hickle-3.4.3-py3-none-any.whl")
	version("3.4.4", sha256="c7305d5cc49df38ce35ff6fbee7264d8d7300057b09f571145ce4d63b4c72e5d", expand=False, url="https://files.pythonhosted.org/packages/c8/b0/c31ea76c3f33680ace47ca3c45fe13d3e9a3ebd3abf2d4b9e3da8be4a1fa/hickle-3.4.4-py2-none-any.whl")
	version("3.4.5", sha256="1a6fcfa9d44c6c0b8a30bc3b0b1ed1e780fa27e2811958d144d4eeb7175fe410", expand=False, url="https://files.pythonhosted.org/packages/b3/45/ebc9e2a77f2349a4947a2eedd4480fc7b248d3f315b0f5a3a1826adcc522/hickle-3.4.5-py3-none-any.whl")
	version("3.4.6", sha256="686998fc9b13899aa4dc293edcb9a602f2b7531c150e061e2c49bc483312435a", expand=False, url="https://files.pythonhosted.org/packages/29/3a/44f729f18d315ed17fc400e643193a7e3136ac3895d9a2447ef09caa3093/hickle-3.4.6-py3-none-any.whl")
	version("3.4.7", sha256="ec07e8f1de8962653160e23c02f2ca24634fb0383caeebe86a80ef9623d2d53d", expand=False, url="https://files.pythonhosted.org/packages/f4/d1/6e45bb57239dc3597e1970b5d2e5f6481f17948ef7944025d52705bdf4f0/hickle-3.4.7-py3-none-any.whl")
	version("3.4.8", sha256="2e154481578de0126561422146c750cb2764acb079519f9304f1ba0964688f9c", expand=False, url="https://files.pythonhosted.org/packages/04/0c/f12327e7f6bc815ea6a028b18f4cf4e06512a7fc4a7623f7a7a35117ff28/hickle-3.4.8-py3-none-any.whl")
	version("3.4.9", sha256="40397b9c5fab04e0770f6a3a1e719e8bca4aea9c6844a7ec1e71b1240ee02e79", expand=False, url="https://files.pythonhosted.org/packages/2a/b0/ad349d5ab32893d1ec8286752d669f2c628696c5b427349e6ef510729e1d/hickle-3.4.9-py3-none-any.whl")
	version("4.0.0", sha256="c9c2c751f239f1fd3ca6daa91fc603027570ea362e6ad8a4e831d75162788c64", expand=False, url="https://files.pythonhosted.org/packages/30/e4/a319d3ee49f53ff20ecf8d698bb6668403bc6156d9cb596af7569b2ad32a/hickle-4.0.0-py3-none-any.whl")
	version("4.0.1", sha256="64cefacfe524bbed79d8303e89805efd15c6c0a8e715dc6d04eec1b6155e6670", expand=False, url="https://files.pythonhosted.org/packages/34/8e/0b0f54bb5758ec641f746b26dcc439a57bf814926b9d7a45fc9d54cee0e6/hickle-4.0.1-py3-none-any.whl")
	version("4.0.2", sha256="9158f20217e5b3286c9da1c4abf34d38721c226f4cd4e71ae1a2fb1414ed7556", expand=False, url="https://files.pythonhosted.org/packages/2e/84/3c3cf512f042feebd4080252e33126c55ec12808335c52fb2bf3c3f0bcd7/hickle-4.0.2-py3-none-any.whl")
	version("4.0.3", sha256="5a5e42bdfd22348ee954c269d01d267b4aa43bbb2455eb5cb07628963c644db3", expand=False, url="https://files.pythonhosted.org/packages/24/c8/af2d17ea98d7eb60ad05689c0509c5c3538a603344818c3d5f0f5c004f1e/hickle-4.0.3-py3-none-any.whl")
	version("4.0.4", sha256="b3a31d88f153eccc62d2aacfa11ed5bed0168d4503d64533594c31f1a353158a", expand=False, url="https://files.pythonhosted.org/packages/42/ee/7f442cb653c22f6f1d9de922919be58d81bc8a09ec4f6d886ce447683596/hickle-4.0.4-py3-none-any.whl")
	version("5.0.0.dev0", sha256="bf8ea1b1a565d3df943d9be0a3f20db31004540c88eadd560a0b5ca353261528", expand=False, url="https://files.pythonhosted.org/packages/4c/bb/178a0dc2bf389712c8395ffbd0f26f489e80fea1f14998f96cd651f05736/hickle-5.0.0.dev0-py3-none-any.whl")
	version("5.0.1", sha256="53601596f9e7f1b0ddab3cf195a4b76cd93b3f708306b44766f32644591681c6", expand=False, url="https://files.pythonhosted.org/packages/7a/f9/e5e5d997ca939be095a72be358f602480633c91234f008ac7fa53a5c0428/hickle-5.0.1-py3-none-any.whl")
	version("5.0.2", sha256="a05f88fe7a4954131ba4dcd6f4701e800c9cb4e45b3d2f50a40403f18b73024d", expand=False, url="https://files.pythonhosted.org/packages/a0/fc/f91e9b1f6f5581b09c91339832a03b4e63444eb1a3565c9d5bad4abaebdd/hickle-5.0.2-py3-none-any.whl")
	version("5.0.3", sha256="3b87613de35e644d94541b8c79ffced5e62332e001b4f62c53ff11bd3fa87dad", expand=False, url="https://files.pythonhosted.org/packages/78/71/d765d1406e2ca52b81f7ff4be6ce99413cb76d831edabf772c667789ff7b/hickle-5.0.3-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-h5py", type=("build", "run"))

# {'numpy': ['3.4.2', '3.4.3', '3.4.4', '3.4.5'], 'h5py': ['3.4.2', '3.4.3', '3.4.4', '3.4.5'], 'dill': ['3.4.4', '3.4.5'], 'dill(>=0.3.0)': ['3.4.6', '3.4.7', '3.4.8', '3.4.9', '4.0.0', '4.0.1', '4.0.2', '4.0.3', '4.0.4', '5.0.0.dev0'], 'h5py(>=2.8.0)': ['3.4.6', '3.4.7', '3.4.8', '4.0.0', '4.0.1'], 'numpy(>=1.8)': ['3.4.6', '3.4.7', '3.4.8', '3.4.9', '4.0.0', '4.0.1', '4.0.2', '4.0.3', '4.0.4'], 'six(>=1.11.0)': ['3.4.6', '3.4.7', '3.4.8', '3.4.9', '4.0.0', '4.0.1', '4.0.2', '4.0.3', '4.0.4'], 'h5py(<3.0.0,>=2.8.0)': ['3.4.9', '4.0.2', '4.0.3', '4.0.4'], 'h5py(>=2.10.0)': ['5.0.0.dev0', '5.0.1', '5.0.2'], 'numpy(!=1.20,>=1.8)': ['5.0.0.dev0', '5.0.1', '5.0.2'], 'h5py>=2.10.0': ['5.0.3'], 'numpy!=1.20,>=1.8': ['5.0.3']}