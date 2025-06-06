# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyYdataProfiling(PythonPackage):
    """Generate profile report for pandas DataFrame"""

    homepage = "https://ydata.ai"
    pypi = "ydata-profiling/ydata_profiling-4.9.0-py2.py3-none-any.whl"

    version(
        "4.0.0",
        sha256="037d941519163c526e339806655e71a714cdbb3d792c7d3002a3eb0e76babe08",
        expand=False,
        url="https://files.pythonhosted.org/packages/38/5f/99628c3bcc8854b4d558823000c00182097e13e9c4c396c0c62d383cbd7d/ydata_profiling-4.0.0-py2.py3-none-any.whl",
    )
    version(
        "4.1.0",
        sha256="de7ee4e4a390a964aa476e3b9b114deaa5654c7885ae0d24fc178f9477dc1c7a",
        expand=False,
        url="https://files.pythonhosted.org/packages/17/e2/e30ceb799bcab62fa4c6fd48ee05b391289cf9467fc17890622ed4e3abfe/ydata_profiling-4.1.0-py2.py3-none-any.whl",
    )
    version(
        "4.1.1",
        sha256="65d62b7d5bc1b4bac3c0122fb07c275796742739ba2c0cd2b2aceddd0ef413eb",
        expand=False,
        url="https://files.pythonhosted.org/packages/61/97/697e458708e6e1aec27527636d955e48120c0a6a266e4de65c8d9a46612c/ydata_profiling-4.1.1-py2.py3-none-any.whl",
    )
    version(
        "4.1.2",
        sha256="8866b96a04e726444f5797477f594393898520b9f0f018d832027b82372d7978",
        expand=False,
        url="https://files.pythonhosted.org/packages/99/a7/daf32ae680605e58fa2a5d33b93f501e5beffac7589c40f284ad5675c214/ydata_profiling-4.1.2-py2.py3-none-any.whl",
    )
    version(
        "4.10.0",
        sha256="569231cd35f8f260829a96129ae3ed1a177ec879b290c2d6fdfde40fe993c5ed",
        expand=False,
        url="https://files.pythonhosted.org/packages/5b/9e/18ace1bd7616642d4a933f2957908b5c6aeb612d1dd0d13c774c8667943f/ydata_profiling-4.10.0-py2.py3-none-any.whl",
    )
    version(
        "4.11.0",
        sha256="d1f2399b1dc5ebe7d6e3091d28a5709cc79c748c776aab0c9280ea837ac00753",
        expand=False,
        url="https://files.pythonhosted.org/packages/2a/b1/f2e328fd01c5a2ae73dd44b3b1c91a35f6ca6acdccff79c083e942bb4e16/ydata_profiling-4.11.0-py2.py3-none-any.whl",
    )
    version(
        "4.12.0",
        sha256="bfc40caaf070ccee55f00d5c09e8954ac2778cce93fbf09de503e3ef5f4d223f",
        expand=False,
        url="https://files.pythonhosted.org/packages/30/b1/527091fffaed57bdf6656edc30dc0e175d5a4936fd44878b8b389303dff9/ydata_profiling-4.12.0-py2.py3-none-any.whl",
    )
    version(
        "4.12.1",
        sha256="c14e148dfc779540203acd17b2298171a72c8098c7e2481f8030f50d6f0dc4b5",
        expand=False,
        url="https://files.pythonhosted.org/packages/a8/e2/91e8ec48c5a9ba759847d74bb69475d22d79922f686e5252d0eb16e5bb85/ydata_profiling-4.12.1-py2.py3-none-any.whl",
    )
    version(
        "4.12.2",
        sha256="b3d2df646a9694dab221d52548ca4d5af0462d5f05996e215fdee35f1e45b391",
        expand=False,
        url="https://files.pythonhosted.org/packages/c5/c9/42ea4945edbd7fac9a8792aaa7647270a56e1a221b573b783957c4286184/ydata_profiling-4.12.2-py2.py3-none-any.whl",
    )
    version(
        "4.13.0",
        sha256="b6f027766bdcdd61f70694b7fa8c4ae3131e0e332aad1dc1797c49bb68c3c42a",
        expand=False,
        url="https://files.pythonhosted.org/packages/47/2b/df2b7563b5f31cac61ae40618703f6a4b470d6e73d91fba67147ebcc4690/ydata_profiling-4.13.0-py2.py3-none-any.whl",
    )
    version(
        "4.14.0",
        sha256="ffabade6d23896308d13df09329185e452a83654443f0daf34541ec20f03e2bb",
        expand=False,
        url="https://files.pythonhosted.org/packages/60/14/09db7a05abc2e49153171e4df3212fe7ced5dca5aa259e31f2bab3efa840/ydata_profiling-4.14.0-py2.py3-none-any.whl",
    )
    version(
        "4.15.0",
        sha256="6f0bc51d4eb0fe34e2df5517aec9b1272383637e763fc46fbf669936725659f4",
        expand=False,
        url="https://files.pythonhosted.org/packages/ac/d7/4114bab39e1db5f56909ba03964ab63c4ca9496af91c00a7c2485c3dab84/ydata_profiling-4.15.0-py2.py3-none-any.whl",
    )
    version(
        "4.15.1",
        sha256="ba0956438fd3e9148ba274d694856dcf4a8bbe74c34cb545cd26f4e525d31d69",
        expand=False,
        url="https://files.pythonhosted.org/packages/4f/5b/22f12322f2d4a71063e6a342635e15ec49f6be5307a9e4a0bd0332fdd572/ydata_profiling-4.15.1-py2.py3-none-any.whl",
    )
    version(
        "4.16.0",
        sha256="7c72a8654f200c2663290e1b35b1148d37a78a6f0d183f96bff5b22b1beca51a",
        expand=False,
        url="https://files.pythonhosted.org/packages/99/33/6e290cb013a00ee2a053d35b112fd8163e137abbb5ff11313b414e414608/ydata_profiling-4.16.0-py2.py3-none-any.whl",
    )
    version(
        "4.16.1",
        sha256="c4655c47f826490c77ea7ca5e9cb613e274db8686ebc095fa01f9735c6466f1f",
        expand=False,
        url="https://files.pythonhosted.org/packages/79/70/1430ad64b36c3d11abd222a95c1568ee56f5a23b07224c699f2b64825bb9/ydata_profiling-4.16.1-py2.py3-none-any.whl",
    )
    version(
        "4.2.0",
        sha256="4355fdea8bc74355bc64a7336229d4ec20ce6d0f55233f5bca0ab564e1d0f9a8",
        expand=False,
        url="https://files.pythonhosted.org/packages/83/28/60d678d1d28196f3bfcc48d13d28aa2fa7906549622e21dc9f90d0a204b2/ydata_profiling-4.2.0-py2.py3-none-any.whl",
    )
    version(
        "4.3.0",
        sha256="e36b792dbabe69be07d04ca9a25e4ec76448f5533caaf222f9f88e185c59fde6",
        expand=False,
        url="https://files.pythonhosted.org/packages/5b/45/8f046f8f39d198fd2fc2060e7f2582a9d2101e3c27574b275d7e2535864d/ydata_profiling-4.3.0-py2.py3-none-any.whl",
    )
    version(
        "4.3.1",
        sha256="45d4ae6a5f6c4b7042de15c39f2c78898039c9e180b7798b437dc925c24a9e69",
        expand=False,
        url="https://files.pythonhosted.org/packages/07/ba/f229e94517d033b427b3e856e1429872ce8368601ef534cad3c14a40f99e/ydata_profiling-4.3.1-py2.py3-none-any.whl",
    )
    version(
        "4.3.2",
        sha256="7f507f510067fe1e9b3763b9d3ef90a129b87351d725afedca25495e79d4296d",
        expand=False,
        url="https://files.pythonhosted.org/packages/37/5e/c9bf58d7a5422001355bb26bfc3a73fc2454f44766c63ac1258e932eb78a/ydata_profiling-4.3.2-py2.py3-none-any.whl",
    )
    version(
        "4.4.0",
        sha256="a49a2b92dc6d3351bc6f52bde9f8e97f91bf5aa3ec176a643736e8b7b50813ac",
        expand=False,
        url="https://files.pythonhosted.org/packages/4b/90/04630cea435fef54d48b0979f1a25b75e541a8140e4e3c63cfda1b00ec7f/ydata_profiling-4.4.0-py2.py3-none-any.whl",
    )
    version(
        "4.5.0",
        sha256="744732ec15d7d909213df7231e0590291b8ce0d6645d31b345982feb6e3d5be9",
        expand=False,
        url="https://files.pythonhosted.org/packages/f6/23/fefced365c9a9f382d0f78a4180b3d52560aa6f924d9e329943acb05db14/ydata_profiling-4.5.0-py2.py3-none-any.whl",
    )
    version(
        "4.5.1",
        sha256="1d810adbd8c8d9113135db641f282b1e5e6df2ec1ae23c6672477393f48803c2",
        expand=False,
        url="https://files.pythonhosted.org/packages/09/98/5a5fbfd48bf23acd3ceed5114d073b877965816304078151fefbf86d8458/ydata_profiling-4.5.1-py2.py3-none-any.whl",
    )
    version(
        "4.6.0",
        sha256="c754e475705c57a1dece77bbcc5445814aa96a52c7ecd6116c0a05b2f46715c8",
        expand=False,
        url="https://files.pythonhosted.org/packages/f5/aa/87674b79a9a364a37ec57cb0c824977c3951020fb2d21e1d8103b428974c/ydata_profiling-4.6.0-py2.py3-none-any.whl",
    )
    version(
        "4.6.1",
        sha256="0421a4a758349a0f6897abaeeb7076d11c40197603b605b773d2d9d90bb2422e",
        expand=False,
        url="https://files.pythonhosted.org/packages/5a/14/a19d2266adf443d441be74d65e4ac12ba252c806ccf7ffdb59c7443bd846/ydata_profiling-4.6.1-py2.py3-none-any.whl",
    )
    version(
        "4.6.2",
        sha256="381ae266b3a2984301976eea0cd845cf1bbc5dcf453902bbac2e9e7a5ae66716",
        expand=False,
        url="https://files.pythonhosted.org/packages/0a/cb/d946b8ab543dfcd6cdf66eb3dfe1d6b39dfdede57b3c8e9115822b3c7bee/ydata_profiling-4.6.2-py2.py3-none-any.whl",
    )
    version(
        "4.6.3",
        sha256="156d68a20f1a1de4c449177291e4eed07e46429d332d162243d8bf2c61f60903",
        expand=False,
        url="https://files.pythonhosted.org/packages/c6/12/a869b9f81c992a179a27d76154b3ae3c1a65a43c9ec117437762093a75ca/ydata_profiling-4.6.3-py2.py3-none-any.whl",
    )
    version(
        "4.6.4",
        sha256="5845e91c58f773f80c2e04602c63992dfe60b9f4ba81be3eec767316091df092",
        expand=False,
        url="https://files.pythonhosted.org/packages/a2/19/c58a6c22a04806c70802518eaf70866e5633fe47e671ded361295dfaf839/ydata_profiling-4.6.4-py2.py3-none-any.whl",
    )
    version(
        "4.6.5",
        sha256="dfeee83a07bc54b6a0894b0ecc52e99afccd0e05b48824db3215560fc8c6cacc",
        expand=False,
        url="https://files.pythonhosted.org/packages/04/45/647c0ebe33584476c335d789a55005683cfa640e07796266de8557560850/ydata_profiling-4.6.5-py2.py3-none-any.whl",
    )
    version(
        "4.7.0",
        sha256="e2044d4483d8fecd2d3a693bc74d8ee80583b82094110157fd698fc8455e10f1",
        expand=False,
        url="https://files.pythonhosted.org/packages/49/03/04ce11264d78f7a9f1025a13f8a078aa18eb2a9c628bc0a9a9c18673062c/ydata_profiling-4.7.0-py2.py3-none-any.whl",
    )
    version(
        "4.8.3",
        sha256="c38e3c839eae547370e6ae3d3f6218d0c7b0a6f9363156f991cd9d3f15bffa34",
        expand=False,
        url="https://files.pythonhosted.org/packages/33/85/45027914eb485482976883dcaab434eab99f1ed5cb222781e7ba46bdf3b7/ydata_profiling-4.8.3-py2.py3-none-any.whl",
    )
    version(
        "4.9.0",
        sha256="af99ec835add3e1f26098a172571175fd1fec5f09d6d650785a620742f156a02",
        expand=False,
        url="https://files.pythonhosted.org/packages/5f/35/d4a9e004206c217bfe8838a37663c1b53769ab839e853c4c250b73968cea/ydata_profiling-4.9.0-py2.py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.7:3.13", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-phik", type=("build", "run"))
    depends_on("py-typeguard@4:", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-pydantic", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-wordcloud", type=("build", "run"))
    depends_on("py-imagehash", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-dacite", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-multimethod", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-visions", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-htmlmin", type=("build", "run"))


# {'scipy(<1.10,>=1.4.1)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2'], 'pandas(!=1.4.0,<1.6,>1.1)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2'], 'matplotlib(<3.7,>=3.2)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2'], 'pydantic(<1.11,>=1.8.1)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2'], 'PyYAML(<6.1,>=5.0.0)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'jinja2(<3.2,>=2.11.1)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'visions[type_image_path](==0.7.5)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'numpy(<1.24,>=1.16.0)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'htmlmin(==0.1.12)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'phik(<0.13,>=0.11.1)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'requests(<2.29,>=2.24.0)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2'], 'tqdm(<4.65,>=4.48.2)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2'], 'seaborn(<0.13,>=0.10.1)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'multimethod(<1.10,>=1.4)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2'], 'statsmodels(<0.14,>=0.13.2)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2'], 'typeguard(<2.14,>=2.13.2)': ['4.0.0', '4.1.0', '4.1.1', '4.1.2'], "jupyter-client(>=5.3.4);extra=='notebook'": ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], "jupyter-core(>=4.6.3);extra=='notebook'": ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], "ipywidgets(>=7.5.1);extra=='notebook'": ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], "tangled-up-in-unicode(==0.2.0);extra=='unicode'": ['4.0.0', '4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'imagehash(==4.3.1)': ['4.1.0', '4.1.1', '4.1.2', '4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'scipy<1.14,>=1.4.1': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.13.0', '4.8.3', '4.9.0'], 'pandas!=1.4.0,<3,>1.1': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'matplotlib<3.10,>=3.5': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.9.0'], 'pydantic>=2': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'PyYAML<6.1,>=5.0.0': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'jinja2<3.2,>=2.11.1': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'visions[type_image_path]<0.7.7,>=0.7.5': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.13.0', '4.7.0', '4.8.3', '4.9.0'], 'numpy<2.2,>=1.16.0': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'htmlmin==0.1.12': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'phik<0.13,>=0.11.1': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'requests<3,>=2.24.0': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'tqdm<5,>=4.48.2': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'seaborn<0.14,>=0.10.1': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.8.3', '4.9.0'], 'multimethod<2,>=1.4': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'statsmodels<1,>=0.13.2': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'typeguard<5,>=3': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.8.3', '4.9.0'], 'imagehash==4.3.1': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'wordcloud>=1.9.3': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'dacite>=1.8': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1', '4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'numba<1,>=0.56.0': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.13.0', '4.14.0', '4.7.0', '4.8.3', '4.9.0'], 'jupyter>=1.0.0;extra=="notebook"': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'ipywidgets>=7.5.1;extra=="notebook"': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'tangled-up-in-unicode==0.2.0;extra=="unicode"': ['4.10.0', '4.11.0', '4.12.0', '4.12.1', '4.12.2', '4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'scipy<1.16,>=1.4.1': ['4.12.2', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'matplotlib>=3.5': ['4.12.2'], 'visions[type_image_path]<0.8.0,>=0.7.5': ['4.12.2'], 'numba<1,>=0.56.0;extra=="numba"': ['4.12.2'], 'pandas!=1.4.0,<3.0,>1.1': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'matplotlib<=3.10,>=3.5': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'black>=20.8b1;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'isort>=5.0.7;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'pre-commit>=2.8.2;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'virtualenv>=20.0.33;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'twine;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'wheel;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'myst-parser>=0.18.1;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'sphinx-rtd-theme>=0.4.3;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'sphinx-autodoc-typehints>=1.10.3;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'sphinx-multiversion>=0.2.3;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'autodoc-pydantic;extra=="dev"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'mkdocs<1.7.0,>=1.6.0;extra=="docs"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'mkdocs-material<10.0.0,>=9.0.12;extra=="docs"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'mkdocs-material-extensions<2.0.0,>=1.1.1;extra=="docs"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'mkdocs-table-reader-plugin<=2.2.0;extra=="docs"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'mike<2.2.0,>=2.1.1;extra=="docs"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'mkdocstrings[python]<1.0.0,>=0.20.0;extra=="docs"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'mkdocs-badges;extra=="docs"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'pyspark>=2.3.0;extra=="spark"': ['4.13.0', '4.14.0'], 'pyarrow>=2.0.0;extra=="spark"': ['4.13.0', '4.14.0'], 'pandas!=1.4.0,<2,>1.1;extra=="spark"': ['4.13.0', '4.14.0'], 'numpy<1.24,>=1.16.0;extra=="spark"': ['4.13.0', '4.14.0'], 'visions[type_image_path]==0.7.5;extra=="spark"': ['4.13.0'], 'pytest;extra=="test"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'coverage<8,>=6.5;extra=="test"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'codecov;extra=="test"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'pytest-cov;extra=="test"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'pytest-spark;extra=="test"': ['4.13.0', '4.14.0'], 'nbval;extra=="test"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'pyarrow;extra=="test"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'twine>=3.1.1;extra=="test"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'kaggle;extra=="test"': ['4.13.0', '4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'visions[type_image_path]<0.8.2,>=0.7.5': ['4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'visions[type_image_path]<0.7.7,>=0.7.5;extra=="spark"': ['4.14.0', '4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'numba<=0.61,>=0.56.0': ['4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'pyspark>=3.0;extra=="spark"': ['4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'pyarrow>=4.0.0;extra=="spark"': ['4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'pandas>1.1;extra=="spark"': ['4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'numpy>=1.16.0;extra=="spark"': ['4.15.0', '4.15.1', '4.16.0', '4.16.1'], 'scipy(<1.11,>=1.4.1)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2'], 'pandas(!=1.4.0,<2,>1.1)': ['4.2.0'], 'matplotlib(<4,>=3.2)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'pydantic(<2,>=1.8.1)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'requests(<3,>=2.24.0)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'tqdm(<5,>=4.48.2)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'multimethod(<2,>=1.4)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'statsmodels(<1,>=0.13.2)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'typeguard(<3,>=2.13.2)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'wordcloud(>=1.9.1)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'dacite(>=1.8)': ['4.2.0', '4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'pandas(!=1.4.0,<2.1,>1.1)': ['4.3.0', '4.3.1', '4.3.2', '4.4.0'], 'scipy(<1.12,>=1.4.1)': ['4.4.0'], 'scipy<1.12,>=1.4.1': ['4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0'], 'pandas!=1.4.0,<2.1,>1.1': ['4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2'], 'matplotlib<4,>=3.2': ['4.5.0', '4.5.1'], 'pydantic<2,>=1.8.1': ['4.5.0', '4.5.1', '4.6.0'], 'visions[type_image_path]==0.7.5': ['4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5'], 'numpy<1.24,>=1.16.0': ['4.5.0', '4.5.1'], 'seaborn<0.13,>=0.10.1': ['4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0'], 'typeguard<3,>=2.13.2': ['4.5.0', '4.5.1'], 'wordcloud>=1.9.1': ['4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], "jupyter-client>=5.3.4;extra=='notebook'": ['4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3'], "jupyter-core>=4.6.3;extra=='notebook'": ['4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3'], "ipywidgets>=7.5.1;extra=='notebook'": ['4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], "tangled-up-in-unicode==0.2.0;extra=='unicode'": ['4.5.0', '4.5.1', '4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3', '4.9.0'], 'matplotlib<=3.7.3,>=3.2': ['4.6.0', '4.6.1', '4.6.2'], 'numpy<1.26,>=1.16.0': ['4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5'], 'typeguard<5,>=4.1.2': ['4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.7.0'], 'numba<0.59.0,>=0.56.0': ['4.6.0', '4.6.1', '4.6.2', '4.6.3', '4.6.4', '4.6.5'], 'matplotlib<3.9,>=3.2': ['4.6.3', '4.6.4', '4.6.5', '4.7.0', '4.8.3'], 'numpy<2,>=1.16.0': ['4.7.0', '4.8.3', '4.9.0'], "jupyter>=1.0.0;extra=='notebook'": ['4.9.0']}
