#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_budget
short_description: Manage a Budget resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Budget resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Budget.
version_added: "2.5"
options:
    compartment_id:
        description:
            - The OCID of the compartment
            - Required for create using I(state=present).
    target_compartment_id:
        description:
            - The OCID of the compartment on which budget is applied
            - Required for create using I(state=present).
    display_name:
        description:
            - The displayName of the budget.
        aliases: ["name"]
    description:
        description:
            - The description of the budget.
    amount:
        description:
            - The amount of the budget expressed as a whole number in the currency of the customer's rate card.
            - Required for create using I(state=present).
        type: float
    reset_period:
        description:
            - The reset period for the budget.
            - Required for create using I(state=present).
        choices:
            - "MONTHLY"
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    budget_id:
        description:
            - The unique Budget OCID
            - Required for update using I(state=present), I(state=absent).
        aliases: ["id"]
    state:
        description:
            - The state of the Budget.
            - Use I(state=present) to create or update a Budget.
            - Use I(state=absent) to delete a Budget.
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create budget
  oci_budget:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    target_compartment_id: ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx
    amount: 10
    reset_period: MONTHLY

- name: Update budget
  oci_budget:
    display_name: display_name_example
    description: description_example
    budget_id: ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete budget
  oci_budget:
    budget_id: ocid1.budget.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
budget:
    description:
        - Details of the Budget resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the budget
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        target_compartment_id:
            description:
                - The OCID of the compartment on which budget is applied
            returned: on success
            type: string
            sample: ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The display name of the budget.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - The description of the budget.
            returned: on success
            type: string
            sample: description_example
        amount:
            description:
                - The amount of the budget expressed in the currency of the customer's rate card.
            returned: on success
            type: float
            sample: 10
        reset_period:
            description:
                - The reset period for the budget.
            returned: on success
            type: string
            sample: MONTHLY
        lifecycle_state:
            description:
                - The current state of the budget.
            returned: on success
            type: string
            sample: ACTIVE
        alert_rule_count:
            description:
                - Total number of alert rules in the budget
            returned: on success
            type: int
            sample: 56
        version:
            description:
                - Version of the budget. Starts from 1 and increments by 1.
            returned: on success
            type: int
            sample: 56
        actual_spend:
            description:
                - The actual spend in currency for the current budget cycle
            returned: on success
            type: float
            sample: 10
        forecasted_spend:
            description:
                - The forecasted spend in currency by the end of the current budget cycle
            returned: on success
            type: float
            sample: 10
        time_spend_computed:
            description:
                - The time that the budget spend was last computed
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_created:
            description:
                - Time that budget was created
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - Time that budget was updated
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "target_compartment_id": "ocid1.targetcompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "amount": 10,
        "reset_period": "MONTHLY",
        "lifecycle_state": "ACTIVE",
        "alert_rule_count": 56,
        "version": 56,
        "actual_spend": 10,
        "forecasted_spend": 10,
        "time_spend_computed": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils, oci_wait_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.budget import BudgetClient
    from oci.budget.models import CreateBudgetDetails
    from oci.budget.models import UpdateBudgetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BudgetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    @staticmethod
    def get_module_resource_id_param():
        return "budget_id"

    def get_module_resource_id(self):
        return self.module.params.get("budget_id")

    def get_get_fn(self):
        return self.client.get_budget

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_budget, budget_id=self.module.params.get("budget_id")
        )

    def list_resources(self):
        required_list_method_params = ["compartment_id"]

        optional_list_method_params = ["display_name"]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(self.client.list_budgets, **kwargs)

    def get_create_model_class(self):
        return CreateBudgetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_budget,
            call_fn_args=(),
            call_fn_kwargs=dict(create_budget_details=create_details),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or oci_common_utils.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateBudgetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_budget,
            call_fn_args=(),
            call_fn_kwargs=dict(
                budget_id=self.module.params.get("budget_id"),
                update_budget_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or oci_common_utils.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_budget,
            call_fn_args=(),
            call_fn_kwargs=dict(budget_id=self.module.params.get("budget_id")),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or oci_common_utils.get_resource_terminated_states(),
        )


BudgetHelperCustom = get_custom_class("BudgetHelperCustom")


class ResourceHelper(BudgetHelperCustom, BudgetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            target_compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            amount=dict(type="float"),
            reset_period=dict(type="str", choices=["MONTHLY"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            budget_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="budget",
        service_client_class=BudgetClient,
        namespace="budget",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
