# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack.package import *


class PyPolars(PythonPackage):
    """Blazingly fast DataFrame library."""

    homepage = "https://www.pola.rs/"
    pypi = "polars/polars-0.20.5.tar.gz"

    license("MIT")

    version("1.27.1", sha256="f801e0d9da198eb97cfb4e8af4242b8396878ff67b655c71570b7e333102b72b", url="https://files.pythonhosted.org/packages/20/c1/c65924c0ca186f481c02b531f1ec66c34f9bbecc11d70246562bb4949876/polars-1.27.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.25.2", sha256="f7fcbb4f476784384ccda48757fca4e8c2e2c5a0a3aef3717aaf56aee4e30e09", url="https://files.pythonhosted.org/packages/cd/92/db411b7c83f694dca1b8348fa57a120c27c67cf622b85fa88c7ecf463adb/polars-1.25.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.20.0", sha256="4996e17cb6f57d9aeaf79f66c54ef2913cea7bd025410c076ef8c05d4f7d792a", url="https://files.pythonhosted.org/packages/2a/1a/862b8bf65182b261022292a1cd49728db876a1ef64ff377d6f7b17653886/polars-1.20.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.19.0", sha256="be0ea51f7b3553652bf0d53f3b925e969a898d4feb9980acecf8e3037d696903", url="https://files.pythonhosted.org/packages/ba/ba/6d715730c28b035abd308fc2cf0fcbae0cedea6216797e83ce4a9a96c6d4/polars-1.19.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.18.0", sha256="a333ff578373e29e0cacc79c35afe42c0620813c9b0c832009ab8b330e421093", url="https://files.pythonhosted.org/packages/f4/cd/cd49096ead3dd208495945021d3042dad01d0dd63702b6f4f4f7e3a3983b/polars-1.18.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.17.1", sha256="59abdab015ed2ecfa0c63862b960816c35096e1f4df057dde3c44cd973af5029", url="https://files.pythonhosted.org/packages/29/08/54fe197c9d5f951cf85944ff9cfe0a706dc9d2230e98814a125eda8a1d09/polars-1.17.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.16.0", sha256="e626d21dcd2566e1442dac414fe177bc70ebfc2f16620d59d778b1b774361018", url="https://files.pythonhosted.org/packages/31/9e/21e05959323883abcee799837d8cac08adf10a48c233432993757e41791a/polars-1.16.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.15.0", sha256="c6686bc8acaaed24f337ae1623536210370ab4d3099c1dbb79ccfc9ec083914a", url="https://files.pythonhosted.org/packages/e3/70/67acead083a0aa6d2717fb35637ba7967d37f4a002527f3d29dc96fb445a/polars-1.15.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.14.0", sha256="0bc46ad6ceeec5d9d881f09c7c1811844e851980735f8455981cdea456e08f5c", url="https://files.pythonhosted.org/packages/dd/3a/f03ee80d8dba47b3fc10d02191ee1690b8d4791626da5ea0a29435bd9b24/polars-1.14.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.13.1", sha256="405826a78c20721d0f47ee58bafdbd5311551c306cc52ff2e8dc0e2f5fc53d07", url="https://files.pythonhosted.org/packages/ce/e8/9fd44ad4c091f911724f4cbe34f960c2e8016391e88f4da75ab0a2b83493/polars-1.13.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.12.0", sha256="afb03647b5160737d2119532ee8ffe825de1d19d87f81bbbb005131786f7d59b", url="https://files.pythonhosted.org/packages/5a/3e/31257118e7e087fa27c230b8fadf8ff15d521140bf58558dc889ee0c9c5e/polars-1.12.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.11.0", sha256="1293f826e5469626d2a4da5e66afb0b46c6f8cb43d16e301d99aa5b911518c34", url="https://files.pythonhosted.org/packages/94/25/7eaafa7320e5bdb88f7f793a08ab0a877309eef1a4537351e362cbd1dcba/polars-1.11.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.10.0", sha256="540051fe456f779b1510c173c3a614135193cf1b94812e11663f65c80dc4626d", url="https://files.pythonhosted.org/packages/28/da/79b54d20c59303864add504a01f927d23415579bdf0a054942bd00da69e3/polars-1.10.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.9.0", sha256="f85f132732aa63c6f3b502b0fdfc3ba9f0b78cc6330059b5a2d6f9fd78508acb", url="https://files.pythonhosted.org/packages/bb/57/b286b317f061d8f17bab4726a27e7b185fbf3d3db65cf689074256ea34a9/polars-1.9.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.8.2", sha256="67c1e448d6e38697650b22dd359f13c40b567c0b66686c8602e4367400e87801", url="https://files.pythonhosted.org/packages/a7/f3/c317b1bc6759d1ec343c25d5ebd376a07a2e1fd2bd04fdc07ce6b2a855c4/polars-1.8.2-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.7.1", sha256="5cd675e4a306b2da57a1b688e65382aaa9e992dd7156b485fbd7f39892a3d784", url="https://files.pythonhosted.org/packages/d5/f4/8cd6d454fcf6e1f5f0a17265a3acca19731f79c65c7432bafbb24492bf73/polars-1.7.1-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.6.0", sha256="a166adb429f8ee099c9d803e7470a80c76368437a8b272c67cef9eef6d5e9da1", url="https://files.pythonhosted.org/packages/04/1c/1a0a0a2c076bec8501ada9496afe5486c9e994558b0c80057f7e3ee6ec16/polars-1.6.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.5.0", sha256="63a242b1cce7bf2502bb68e269b01b593068c798b47025fb17ac5b89603e9d8f", url="https://files.pythonhosted.org/packages/e4/a4/0eadfba75a12366af2f0554649aa69c319fb85111025d8583f0b21d0e0c0/polars-1.5.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.4.1", sha256="7cf834a328e292c31c06eb606496becb6d8a795e927c826e26e2af27087950f1", url="https://files.pythonhosted.org/packages/ef/52/86e6d9a264d0a5b13f2a813f1efab82fd63151852936c1413195d75ec6ee/polars-1.4.1-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.3.0", sha256="9a1ff7779315e6b0d17641af3eb4dd7aec2ab0bc1bee009efb12242bf6403aeb", url="https://files.pythonhosted.org/packages/e3/b3/f32a2f3e2881e45878c9f1fe18ea63d1208631b998965fb84c81b0e8824c/polars-1.3.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.2.1", sha256="2094877da694bb59bfb7f5af50471955012b950068dc6f3ef5ecc41653a3b04f", url="https://files.pythonhosted.org/packages/ff/34/85fd0e2bbcfe24ed8963d988336996c2c7be96a70371cd6225d4e75f324b/polars-1.2.1-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.1.0", sha256="967ee75160315e881e414bbb3198b5534d6ea4a086f06fa8fdfb4cd95a2b8e8f", url="https://files.pythonhosted.org/packages/db/94/618144499355900ffe0f5e496819cb0266a9e1845b6653ae574bd7965dc3/polars-1.1.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("1.0.0", sha256="f5b58575fd7ddc12bc53adfde933da3b40c2841fdc5396fecbd85e80dfc9332e", url="https://files.pythonhosted.org/packages/75/a2/d0b30ea916f1008de668c16f037c7585b82798e649b7cceaa7f8fd140efa/polars-1.0.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)
    version("0.20.31", sha256="24b82441f93409e0e8abd6f427b029db102f02b8de328cee9a680f84b84e3736", url="https://files.pythonhosted.org/packages/90/7d/7541e559d7fce232ba34340b0953cac9af2344853d675dc2de01a4d3abc7/polars-0.20.31-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", expand=False)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import polars as pl; print(pl.__version__)")
