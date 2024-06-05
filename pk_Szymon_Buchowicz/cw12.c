#include <stdio.h>
#include <stdlib.h>
#include "cw12.h"

node *create_node(int value)
{
    node* newNode = malloc(sizeof(node));
    if(newNode == NULL){
        return NULL;
    }
    newNode->value = value;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

node *insertLeft(node *root, int value)
{
    root->left = create_node(value);
    return root->left;
}

node *insertRight(node *root, int value)
{
    root->right = create_node(value);
    return root->right;
}

void preorder_travelsal(node *root){
    if (root == NULL){return;}
    printf("%d ->", root->value);  //(*root).value
    preorder_travelsal(root->left);
    preorder_travelsal(root->right);
}

void inorder_travelsal(node *root){
    if(root == NULL) {return;}
    inorder_travelsal(root->left);
    printf("%d -> ", root->value);
    inorder_travelsal(root->right);
}

void postorder_travelsal(node *root){
    if(root == NULL) {return;}
    inorder_travelsal(root->left);
    inorder_travelsal(root->right);
    printf("%d -> ", root->value);
}

void test_binary_tree()
{
    node *root = create_node(1);
    if (root == NULL) { return;}
    node *n1left = insertLeft(root, 3);
    node *n1right = insertRight(root, 5);
    if(n1left != NULL){
        insertLeft(root->left, 10);
        insertRight(root->left, 19);
    }
    if(n1right != NULL){
        insertLeft(root->right, 13);
        insertRight(root->right, 8);
    }
    preorder_travelsal(root);
    printf("\n\n");
    inorder_travelsal(root);
    printf("\n\n");
    postorder_travelsal(root);
}



int main()
{
    test_binary_tree();
    return 0;
}